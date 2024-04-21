#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Update system package list
echo "Updating package list..."
sudo apt-get update

# Install FFmpeg
echo "Installing FFmpeg..."
sudo apt-get install -y ffmpeg

# Install Python dependencies from requirements.txt
echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Setup completed successfully."
