#!/bin/bash

echo "================================================"
echo "   AgriSense - AI Crop Recommendation System"
echo "================================================"
echo ""

# Check if Python is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
else
    echo "❌ Error: Python is not installed!"
    echo "Please install Python 3.8 or higher first."
    exit 1
fi

echo "✓ Python found: $PYTHON_CMD"
echo ""

# Check if models directory exists and has model files
if [ ! -f "models/rf_model.pkl" ]; then
    echo "📦 Model not found. Training model first..."
    echo ""
    $PYTHON_CMD model_training.py

    if [ $? -ne 0 ]; then
        echo ""
        echo "❌ Model training failed!"
        echo "Please check the error messages above."
        exit 1
    fi
    echo ""
    echo "✓ Model trained successfully!"
else
    echo "✓ Model already trained"
fi

echo ""
echo "🚀 Starting AgriSense web application..."
echo ""
echo "================================================"
echo "   Server will start on http://localhost:5000"
echo "   Press Ctrl+C to stop the server"
echo "================================================"
echo ""

$PYTHON_CMD app.py
