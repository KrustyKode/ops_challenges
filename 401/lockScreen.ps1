# Script Name:                  lockScreen.ps1
# Author:                       Michael Sineiro
# Date of latest revision:      1/18/2024
# Purpose:                      configures auto-lock-screen, windows scans, and OS updates.
<# I used the following websites for reference.  
https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/use-powershell-cmdlets-microsoft-defender-antivirus?view=o365-worldwide
https://www.parallels.com/blogs/ras/powershell-windows-update/

#>   

# Store the current execution policy
$originalExecutionPolicy = Get-ExecutionPolicy

# Set the execution policy to Bypass for the duration of the script
Set-ExecutionPolicy Bypass -Scope Process -Force

# Install PSWindowsUpdate module if not already installed
if (-not (Get-Module -ListAvailable -Name PSWindowsUpdate)) {
    Install-Module -Name PSWindowsUpdate -Force -AllowClobber
}

function Show-Menu {
    Clear-Host
    Write-Host "SOC 2 Configuration Script"
    Write-Host "1. Set Automatic Screen Lock"
    Write-Host "2. Schedule Windows Defender Scan"
    Write-Host "3. Enable Automatic OS Updates"
    Write-Host "4. Exit"
}

function Set-ScreenLock {
    # Set automatic screen lock
    $registryPath = "HKCU:\Control Panel\Desktop"
    $registryName = "ScreenSaveActive"

    # Check if the registry key exists, if not, create it
    if (-not (Test-Path $registryPath)) {
        New-Item -Path $registryPath -Force
    }

    # Enable screen saver
    Set-ItemProperty -Path $registryPath -Name $registryName -Value 1

    # Set screen saver timeout to 600 seconds (10 minutes)
    $timeoutRegistryPath = "HKCU:\Control Panel\Desktop"
    $timeoutRegistryName = "ScreenSaveTimeOut"

    # Check if the registry key exists, if not, create it
    if (-not (Test-Path $timeoutRegistryPath)) {
        New-Item -Path $timeoutRegistryPath -Force
    }

    # Set screen saver timeout to 600 seconds
    Set-ItemProperty -Path $timeoutRegistryPath -Name $timeoutRegistryName -Value 600

    Write-Host "Automatic Screen Lock configured successfully."
}

function Schedule-DefenderScan {
    # Schedule Windows Defender scan every Friday at 11pm
    $defenderSchedule = New-ScheduledTaskAction -Execute "C:\Program Files\Windows Defender\MpCmdRun.exe" -Argument "-Scan -ScanType 2"
    $trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Friday -At 23:00
    Register-ScheduledTask -Action $defenderSchedule -Trigger $trigger -TaskName "WindowsDefenderScan"

    Write-Host "Windows Defender Scan scheduled successfully."
}

function Enable-OSUpdates {
    # Enable automatic OS updates using Get-WindowsUpdate cmdlet
    try {
        # Import the PSWindowsUpdate module
        Import-Module PSWindowsUpdate -Force

        # Check for and install updates
        $updates = Get-WindowsUpdate -Install -AcceptAll -AutoReboot

        if ($updates.Count -gt 0) {
            Write-Host "Automatic OS Updates enabled successfully. Installed $($updates.Count) updates."
        } else {
            Write-Host "No updates found."
        }
    } catch {
        Write-Host "Error: $_"
    }
}

# Main script loop
do {
    Show-Menu
    $choice = Read-Host "Enter your choice (1-4):"

    switch ($choice) {
        1 { Set-ScreenLock }
        2 { Schedule-DefenderScan }
        3 { Enable-OSUpdates }
        4 { exit }
        default { Write-Host "Invalid choice. Please enter a valid option." }
    }

    $null = Read-Host "Press Enter to continue..."

} while ($choice -ne 4)

# Reset the execution policy to its original state
Set-ExecutionPolicy $originalExecutionPolicy -Scope Process -Force
