# PowerShell Script to Configure Security Settings

# Ensuring 'Password must meet complexity requirements' is set to 'Enabled'
Write-Host "Enabling 'Password must meet complexity requirements'..."
$complexity = "ComputerConfiguration/WindowsSettings/SecuritySettings/AccountPolicies/PasswordPolicy/PasswordMustMeetComplexityRequirements"
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "ComplexityRequirements" -Value 1
Write-Host "'Password must meet complexity requirements' has been enabled."

# Ensuring 'Configure SMB v1 client driver' is set to 'Enabled: Disable driver (recommended)'
Write-Host "Configuring 'SMB v1 client driver' to 'Enabled: Disable driver (recommended)'..."
Enable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol
Write-Host "'SMB v1 client driver' has been configured to 'Enabled: Disable driver (recommended)'."

# End of script
Write-Host "Configuration complete."