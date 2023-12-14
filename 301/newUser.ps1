Import-Module ActiveDirectory

# Script Name:                  standUP.ps1
# Author:                       Michael Sineiro
# Date of latest revision:      12/13/2023
# Purpose:                      add a user to active directory 
# I refereced this guide https://learn.microsoft.com/en-us/powershell/module/activedirectory/?view=windowsserver2022-ps

# Read user input
# Read user input
$fullName = Read-Host "Enter full name (First Last):"
$username = Read-Host "Enter desired username:"
$email = Read-Host "Enter email address (UPN will be derived):"
$department = Read-Host "Enter department (optional):"
$location = Read-Host "Enter location (optional):"
$title = Read-Host "Enter job title (optional):"
$company = Read-Host "Enter company (optional):"

# Extract first and last name from full name
$firstName = $fullName.Split(" ")[0]
$lastName = $fullName.Split(" ")[-1]

# Validate email address format
if (!([System.Net.Mail.MailAddress]::IsValid($email))) {
  Write-Error "Invalid email address format!"
  exit
}

# Create AD user
try {
  New-ADUser
    -Name "$firstName $lastName"
    -SamAccountName $username
    -UserPrincipalName "$email"
    -EmailAddress $email
    -Department $department
    -Location $location
    -Title $title
    -Company $company
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

# Clean up temporary variables (optional)
# $firstName, $lastName, $email, $username, $user
