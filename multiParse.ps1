# Script Name:                  multiParse,ps1
# Author:                       Michael Sineiro
# Date of latest revision:      11/3/2023
# Purpose:                      a few short scripts


# Decleration of variables

# Decleration of functions

# Main

# Print to the terminal screen all active processes ordered by highest CPU time consumption
Get-Process | Sort-Object -Descending CPU | Select-Object -ExpandProperty Name

# Print to the terminal screen all active processes ordered by highest Process Identification Number 
Get-Process | Sort-Object -Descending ID | Select-Object -ExpandProperty Name

# Print to the terminal screen the top five active processes ordered by highest Working Set
Get-Process | Sort-Object -Descending WorkingSet | Select-Object -First 5 -ExpandProperty Name

# Start a browser process 
Start-Process -FilePath "chrome.exe" -ArgumentList "https://owasp.org/www-project-top-ten/"

# I set the notepad count to 10 and i to 0
$notepadCount = 10
for ($i = 0; $i -lt $notepadCount; $i++) {  # while i < 10 the loop will increment 
    Start-Process -FilePath "notepad.exe"  # opens notepad
}

# Close all instances of the Notepad
Get-Process -Name notepad | Stop-Process

# Kill a process by its Process Identification Number
Stop-Process -Id 12345

# End


