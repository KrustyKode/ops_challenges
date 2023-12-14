Import-Module ActiveDirectory

# Script Name:                  standUP.ps1
# Author:                       Michael Sineiro
# Date of latest revision:      11/6/2023
# Purpose:                      add a user to active directory 
# I refereced this guide https://learn.microsoft.com/en-us/powershell/module/activedirectory/?view=windowsserver2022-ps

# Read user input
$firstName = Read-Host "Enter first name:"
$lastName = Read-Host "Enter last name:"
$email = Read-Host "Enter email address (username will be derived):"

# Validate email address format
if (!([System.Net.Mail.MailAddress]::IsValid($email))) {
  Write-Error "Invalid email address format!"
  exit
}

# Extract username from email
$username = $email.Split("@")[0]

# Create AD user
try {
  New-ADUser
    -Name "$firstName $lastName"
    -SamAccountName $username
    -UserPrincipalName "$email"
    -EmailAddress $email
    -Department "TPS"
    -Location "Springfield, OR"
    -Title "TPS Reporting Lead"
    -Company "GlobeX USA"
    -Enabled $true
  Write-Host "User '$firstName $lastName' created successfully!"
}
catch {
  Write-Error "Error creating user: $_"
}

# Verify user creation in ADAC
$user = Get-ADUser -Filter "SamAccountName -eq '$username'"
if ($user) {
  Write-Host "User '$firstName $lastName' verified in AD."
} else {
  Write-Error "User '$firstName $lastName' not found in AD."
}

# Pause for user review before exiting
Read-Host "Press any key to exit..."
