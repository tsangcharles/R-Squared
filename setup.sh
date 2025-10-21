#!/bin/bash

# Setup script for R-Squared Analysis Project
# This script creates a virtual environment and installs dependencies

set -e  # Exit on error

PROJECT_NAME="r_squared_analysis"
VENV_DIR="venv"
PYTHON_VERSION="python3"

echo "=========================================="
echo "R-Squared Analysis - Environment Setup"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v $PYTHON_VERSION &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3 before running this script"
    exit 1
fi

echo "✓ Python found: $($PYTHON_VERSION --version)"
echo ""

# Create virtual environment
if [ -d "$VENV_DIR" ]; then
    echo "⚠ Virtual environment already exists in '$VENV_DIR'"
    read -p "Do you want to remove it and create a new one? (y/N) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Removing existing virtual environment..."
        rm -rf "$VENV_DIR"
    else
        echo "Keeping existing virtual environment"
        echo "Skipping to dependency installation..."
    fi
fi

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in '$VENV_DIR'..."
    $PYTHON_VERSION -m venv "$VENV_DIR"
    echo "✓ Virtual environment created"
fi

echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

echo ""

# Install dependencies
echo "Installing dependencies..."
pip install pandas scikit-learn numpy matplotlib

echo ""
echo "✓ All dependencies installed successfully!"
echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "To activate the virtual environment, run:"
echo "  source $VENV_DIR/bin/activate"
echo ""
echo "To run the analysis, execute:"
echo "  python main.py"
echo ""
echo "To deactivate the virtual environment when done:"
echo "  deactivate"
echo ""
