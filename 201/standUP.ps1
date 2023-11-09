# Script Name:                  standUP.ps1
# Author:                       Michael Sineiro
# Date of latest revision:      11/6/2023
# Purpose:                      enable, disable and remove  
### I grabbed all these commands from the following page: https://github.com/superswan/Powershell-SysAdmin

# Enable File and Printer Sharing

Set-NetFirewallRule -DisplayGroup "File And Printer Sharing" -Enabled True

# Allow ICMP traffic

netsh advfirewall firewall add rule name="Allow incoming ping requests IPv4" dir=in action=allow protocol=icmpv4 

# Enable Remote management

reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f

# Remove bloatware

iex ((New-Object System.Net.WebClient).DownloadString('https://git.io/debloat'))

# Enable Hyper-V

Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All

# Disable SMBv1

Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force


