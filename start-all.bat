@echo off
echo Starting Glaucoma Detection Project...
echo.
echo Starting Backend API...
start "Glaucoma API Backend" cmd /k "cd glaucoscan-API && python app.py"
timeout /t 5 /nobreak >nul
echo.
echo Starting Frontend UI...
start "Glaucoma UI Frontend" cmd /k "cd glaucoscan-UI && npm run dev"
echo.
echo Both services are starting in separate windows.
echo Backend will be available at: http://localhost:8236
echo Frontend will be available at: http://localhost:3000
echo.
echo Press any key to exit this window (services will continue running)...
pause >nul

