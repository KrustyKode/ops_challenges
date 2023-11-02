# Script: logs.ps1
# Author: Michael Sineiro
# Date: 11/2/2023
# Purpose: pulls system logs.

# main

# takes all system events that occured in the last 24 hours and places them in a last_24

Get-EventLog -LogName System -Newest 24 | Out-File -FilePath "$env:USERPROFILE\Desktop\last_24.txt"


# takes all “error” type events from the System event log to a file on your desktop named errors.txt.

Get-EventLog -LogName System | Where-Object {$_.EntryType -eq "Error"} | 
Out-File -FilePath "$env:USERPROFILE\Desktop\errors.txt"


# Print to the screen all events with ID of 16 from the System event log.

Get-EventLog -LogName System | Where-Object {$_.EventID -eq 16} 


# Print to the screen the most recent 20 entries from the System event log.

Get-EventLog -LogName System | Sort-Object -Descending TimeGenerated | Select-Object -First 20


# Print to the screen all sources of the 500 most recent entries in the System event log.
# Ensure that the full lines are displayed (get rid of the … and show the entire text).

get-eventlog -logname system -newest 500 | select-object -property source | format-table -autosize

# end