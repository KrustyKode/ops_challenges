# Script Name:                  lockScreen.ps1
# Author:                       Michael Sineiro
# Date of latest revision:      1/18/2024
# Purpose:                      automatically set a screen lockout timer



# PowerShell script to automate Screen Lock on Windows 10

# Set the screen lock timeout value (in seconds)
$timer = 300

# Set the registry path for screen lock timeout
$regPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"

# Create a new registry key if it doesn't exist
if (-not (Test-Path $regPath)) {
    New-Item -Path $regPath -Force
}

# Set the screen lock timeout in the registry
New-ItemProperty -Path $regPath -Name InactivityTimeout -Value $timer -PropertyType DWORD -Force

# Display a message indicating successful configuration
Write-Host "Automatic Screen Lock timeout configured successfully to $timer seconds."
