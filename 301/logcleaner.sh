#!/bin/bash

# Script Name:                  logCleaner.sh
# Author:                       Michael Sineiro
# Date of latest revision:      12/1/2023
# Purpose:                      compare file, make dir, zip it up, wipe it,
########                        compare again!
# Execution:                    bash logCleaner.sh ./logCleaner.sh chmod -x logCleaner.sh


# FUNctions to print the file size of the log files
function logFiles() {
  echo "File size of syslog.log:"
  # disk use | -h makes it easy to read 👀 
  du -h /var/log/syslog
  echo "File size of wtmp.log:"
  du -h /var/log/wtmp
}

# FUNctions to create a backup directory
function backupDir() {
  mkdir -p /var/log/backups
}

# FUNctions to compress the contents of the log files to the backup directory
function cOmPrEss() {
# self explanitory
  stamp=$(date +"%Y%m%d @ %H%M%S")
# zips and overwrites specified files
  gzip -c /var/log/syslog > /var/log/backups/syslog-$stamp.zip
  gzip -c /var/log/wtmp > /var/log/backups/wtmp-$stamp.zip
}

# FUNctions to clear the contents of the log files
function wipe() {
# set file to zero bytes 
  truncate -s 0 /var/log/syslog
  truncate -s 0 /var/log/wtmp
}

# FUNctions to print the file size of the compressed files
function newFileSize() {
  echo "File size of syslog.log.zip:"
  du -h /var/log/backups/syslog-$stamp.zip
  echo "File size of wtmp.log.zip:"
  du -h /var/log/backups/wtmp-$stamp.zip
}

# FUNctions to compare the size of the compressed files to the size of the original log files
function comparing() {
  echo "Comparison of compressed file sizes to original log file sizes:"
  echo "syslog.log.zip / syslog.log:"
  du -h /var/log/backups/syslog-$stamp.zip /var/log/syslog
  echo "wtmp.log.zip / wtmp.log:"
  du -h /var/log/backups/wtmp-$stamp.zip /var/log/wtmp
}

# Call the functions to perform the tasks
logFiles
backupDir
cOmPrEss
wipe
newFileSize
comparing
