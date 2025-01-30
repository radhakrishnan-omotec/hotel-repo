#!/bin/bash

# Set environment variables for Python (optional)
export PYTHONPATH=/usr/local/lib/python3.8/dist-packages

# Ensure DISPLAY is set correctly for Raspberry Pi (if applicable)
export DISPLAY=:0


# Check if the required Python dependencies are installed
echo "Checking for required dependencies..."


# Check if OpenCV is installed, install if it's not
if ! python3 -c "import cv2" &> /dev/null; then
    echo "OpenCV not found. Installing OpenCV..."
    pip install opencv-python
fi

# Check if the required files exist
if [ ! -f "image_data1.db" ]; then
    echo "Error: /image_data1.db not found!"
    exit 1
fi


# Run the Python script
echo "Starting Hotel Project Python script..."
python3 main.py

echo "End of Project Python script..."