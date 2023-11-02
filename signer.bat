@echo off

REM Get user input
set /p name="Enter your name: "
set /p job_title="Enter your job title: "
set /p department="Enter your department: "

REM Create the email signature
set signature="
<p>
    Sincerely,
    <br>
    <strong style='font-size: 16px;'>$name</strong>
    <br>
    $job_title
    <br>
    $department
</p>
"

REM Save the email signature to a file
echo $signature > "%userprofile%\AppData\Roaming\Thunderbird\Profiles\default\Mail\Signatures\signature.html"

REM Display a success message
echo "Your email signature has been created successfully!"
pause