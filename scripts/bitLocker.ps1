# PowerShell script to enable BitLocker on the C: drive without TPM

# Specify the drive letter
$driveLetter = "C:"

# Check if BitLocker is already enabled
$bitLockerStatus = Get-BitLockerVolume -MountPoint $driveLetter
if ($bitLockerStatus.ProtectionStatus -eq "On") {
    Write-Host "BitLocker is already enabled on the drive $driveLetter"
    exit
}

# Prompt the user to enter a password
$password = Read-Host "Enter a password for BitLocker encryption"

# Convert the password to a secure string
$securePassword = ConvertTo-SecureString $password -AsPlainText -Force

# Enable BitLocker using a password protector
Enable-BitLocker -MountPoint $driveLetter -PasswordProtector -Password $securePassword -UsedSpaceOnly -SkipHardwareTest

Write-Host "BitLocker has been enabled on the drive $driveLetter"
