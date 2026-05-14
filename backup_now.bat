@echo off
setlocal

for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd_HHmmss"') do set ts=%%i

set BACKUP_DIR=_backups\%ts%
mkdir "%BACKUP_DIR%"

xcopy "registry" "%BACKUP_DIR%\registry\" /E /I /H /Y >nul
xcopy "config" "%BACKUP_DIR%\config\" /E /I /H /Y >nul

if exist "db.sqlite3" copy /Y "db.sqlite3" "%BACKUP_DIR%\db.sqlite3" >nul
if exist "manage.py"  copy /Y "manage.py"  "%BACKUP_DIR%\manage.py" >nul

echo.
echo ✅ Backup created: %BACKUP_DIR%
echo.
endlocal
