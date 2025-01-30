@echo off
setlocal

:: Set environment variables for Python (optional)
set PYTHONPATH=C:\Path\To\Python\Lib\site-packages

:: Ensure required dependencies are installed
echo Checking for required dependencies...

:: Check if OpenCV is installed
python -c "import cv2" 2>NUL
if %errorlevel% neq 0 (
    echo OpenCV not found. Installing OpenCV...
    pip install opencv-python
)

:: Check if the required file exists
if not exist "image_data1.db" (
    echo Error: image_data1.db not found!
    exit /b 1
)

:: Run the Python script
echo Starting Hotel Project Python script...
python main.py

echo End of Project Python script...
endlocal
pause



:: How to Use:
:: Copy the above script into a text file and save it as package.bat.
:: Run the .bat file by double-clicking it or executing it via the Command Prompt.
:: Ensure Python and pip are installed and available in the system PATH.