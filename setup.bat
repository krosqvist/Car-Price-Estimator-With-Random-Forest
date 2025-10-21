@echo off
REM --- Force script to use its own folder as working directory ---
pushd "%~dp0"
echo Current working directory: %cd%
echo.

REM ==========================================
REM  Car Price Estimator - Setup & Run Script
REM ==========================================
echo.
echo Setting up Car Price Estimator
echo ==========================================
echo.

REM --- Check Python ---
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python not found. Please install Python 3.8+ and re-run this script.
    pause
    exit /b
)

REM --- Check Node ---
where node >nul 2>nul
if %errorlevel% neq 0 (
    echo Node.js not found. Please install Node.js and re-run this script.
    pause
    exit /b
)

REM --- Create virtual environment if not exist ---
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM --- Activate venv ---
call venv\Scripts\activate

REM --- Upgrade pip ---
echo Upgrading pip...
python -m pip install --upgrade pip

REM --- Install backend Python dependencies ---
if exist Backend\requirements.txt (
    echo Installing backend dependencies...
    python -m pip install -r Backend\requirements.txt
) else (
    echo Backend\requirements.txt not found. Skipping Python dependency install.
)

REM --- Install Node.js dependencies ---
if exist Backend\package.json (
    echo Installing Node.js backend dependencies...
    cd Backend
    npm install
    cd ..
) else (
    echo Could not find Backend\package.json.
    pause
    exit /b
)

REM --- Start backend server ---
if exist Backend\server.js (
    echo Starting Node.js backend server...
    cd Backend
    REM Keep venv active and run npm dev in same window
    npm run dev
) else (
    echo Could not find Backend\server.js
    pause
    exit /b
)
