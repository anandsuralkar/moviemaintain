# Get the directory of the current script
$ScriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Change directory to the desired folder
Set-Location -Path "$ScriptDirectory"

# Launch first terminal window and run commands
Start-Process -NoNewWindow powershell -ArgumentList "-NoExit", "-Command", ".\envi\Scripts\activate ; cd movieproject ; python manage.py runserver"

# Launch second terminal window and run commands
Start-Process -NoNewWindow powershell -ArgumentList "-NoExit", "-Command", ".\envi\Scripts\activate ; cd moviemaintain\appfront ; ng serve --open"
