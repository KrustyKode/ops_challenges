# Script Name:                  addressing.ps1
# Author:                       Michael Sineiro
# Date of latest revision:      12/18/2023
# Purpose:                     creates new domain and forest

Add-WindowsFeature RSAT-AD-PowerShell
# Prompt the user for input
$domainName = Read-Host -Prompt "Enter the domain name"
$netBIOSName = Read-Host -Prompt "Enter the NetBIOS name"

# Install the required Windows features
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

# Promote the server to a domain controller and configure Active Directory Forest
Install-ADDSForest `
    -DomainName $domainName `
    -DomainMode "WinThreshold" `
    -ForestMode "WinThreshold" `
    -DomainNetbiosName $netBIOSName `
    -InstallDns:$true `
    -Force:$true

# Restart the server to complete the installation
Restart-Computer -Force
