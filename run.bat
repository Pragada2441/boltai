@echo off
echo ================================================
echo    AgriSense - AI Crop Recommendation System
echo ================================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed!
    echo Please install Python 3.8 or higher first.
    pause
    exit /b 1
)

echo [OK] Python found
echo.

REM Check if model exists
if not exist "models\rf_model.pkl" (
    echo [INFO] Model not found. Training model first...
    echo.
    python model_training.py

    if %errorlevel% neq 0 (
        echo.
        echo [ERROR] Model training failed!
        echo Please check the error messages above.
        pause
        exit /b 1
    )
    echo.
    echo [OK] Model trained successfully!
) else (
    echo [OK] Model already trained
)

echo.
echo [INFO] Starting AgriSense web application...
echo.
echo ================================================
echo    Server will start on http://localhost:5000
echo    Press Ctrl+C to stop the server
echo ================================================
echo.

python app.py
pause
