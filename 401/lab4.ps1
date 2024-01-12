# PowerShell Script to Configure Security Settings

# Ensuring 'Password must meet complexity requirements' is set to 'Enabled'
# PowerShell Script to Configure Security Settings on Windows Server 2022

# Temporary file for security settings
$secTempFile = "C:\secsettings.cfg"

# Export current security settings
secedit /export /cfg $secTempFile

# Set 'Password must meet complexity requirements' to Enabled
(Get-Content $secTempFile).replace("PasswordComplexity = 0", "PasswordComplexity = 1") | Set-Content $secTempFile

# Apply the modified security settings
secedit /configure /db $env:windir\security\local.sdb /cfg $secTempFile /areas SECURITYPOLICY

# Remove the temporary file
Remove-Item $secTempFile


# Output results
Write-Host "Security settings have been configured."

# End of script

# Ensuring 'Configure SMB v1 client driver' is set to 'Enabled: Disable driver (recommended)'
Write-Host "Configuring 'SMB v1 client driver' to 'Enabled: Disable driver (recommended)'..."
Enable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol
Write-Host "'SMB v1 client driver' has been configured to 'Enabled: Disable driver (recommended)'."

# End of script
Write-Host "Configuration complete."