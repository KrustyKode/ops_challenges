# "@echo off" dsables echoing inside of this script
@echo off
# enabling delayed expansion, variables will be expanded after current line is run.
setlocal enabledelayedexpansion

# prompting user to "Enter the SOURCE folder path:" and stores it in sourcePath.
set /p sourcePath=Enter the source folder path:

# prompting user to Enter the DESTINATION folder path:" and stores it in destinationPath.
set /p destinationPath=Enter the destination folder path:

# If loop that states if the users selected sourcePath does not exist
# The first line contains an open parathesis, this indicates the begining of the body of the loop.
if not exist "!sourcePath!\" (
# if the path does not exist then a message displaying "Error: Source folder does not exist." shows.
    echo Error: Source folder does not exist.
# "goto :eof" exits the batch file
    goto :eof
# the closed parenthesis ends the body of the loop.
)

# another if loop, this one does the same procedure for the "destinationPath" veriable.
if not exist "!destinationPath!\" (
# if the path does not exist then a message displaying "Error: Destination folder does not exist." shows.
    echo Error: Destination folder does not exist.
# "goto :eof" exits the batch file
    goto :eof
)
# the robocopy command is being told to copy from "!sourcePath!" to "!destinationPath!"
# "/E" is a switch used to specify that all subdirectories should be copied, including blank ones.
robocopy "!sourcePath!" "!destinationPath!" /E

# errorlevel is used to indicate if a command is succesful or not.
# errorlevel 1 or above indicates some sort error occured.
if errorlevel 8 (
# if 8 is returned for the errorLevel then the message
# "Error: ROBOCOPY encountered errors during the copy operation." will display.
    echo Error: ROBOCOPY encountered errors during the copy operation.
# if the errorLevel is not 8 the else statement will be executed.
) else ( 
# which will display the following message "Copy operation completed successfully."
    echo Copy operation completed successfully.
)
# This line indicates the end of the script 
# and also turns our local "enabledelayedexpansion" back off.
endlocal