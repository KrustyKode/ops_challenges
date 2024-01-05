<#
This script takes a backup copy of an entire folder and puts it on a dedicated backup drive.
It is recommended to use an external hard drive for this backup.
To correctly use this script, be sure that you format each backup drive with the $BkupVolumeLabel keyword in the Volume Label.

To run the script automatically:
Schedule a task to run program powershell.exe with the argument:
-executionpolicy Bypass -file "[insert path to script file here]"

Schedule to run as often as you would like to make a backup.
#>

$SourcePath = "C:\Users"

$BkupVolumeLabel = "Offsite"

$RetentionDays = 7

#########################################
####### I WILL TAKE IT FROM HERE! #######
#########################################
$Date = Get-Date -Format "yyyy MMM dd hhmm tt"
$BackupDrives = (Get-Volume | Where-Object {$_.FileSystemLabel -like "*$BkupVolumeLabel*"}).DriveLetter

ForEach ($Drive in $BackupDrives) {
    $Letter = "$Drive" + ":\"
    $Destination = "$Letter" + (Get-Item -Path $SourcePath).Name
    IF (-not (Test-Path -Path $Destination)) {
        New-Item -Path $Destination -ItemType Directory
    }
    Copy-Item -Path $SourcePath -Destination "$Destination\$date" -Recurse
    Get-ChildItem -Path $Destination | Where-Object {$_.CreationTime -lt ((Get-Date).AddDays( - $RetentionDays))} | Remove-Item -Force -Recurse
}

#$Error > C:\users\public\desktop\BackupErrors.txt #Remove leading # if you need error information for failed backups.