# Setup Instructions for AgriSense

## Quick Start Guide

### Step 1: Install Python Dependencies

Run one of the following commands based on your system:

```bash
# Option 1: Using pip
pip install -r requirements.txt

# Option 2: Using pip3
pip3 install -r requirements.txt

# Option 3: Using python module
python -m pip install -r requirements.txt

# Option 4: Using python3 module
python3 -m pip install -r requirements.txt
```

### Step 2: Train the Machine Learning Model

```bash
python model_training.py
```

**Expected Output:**
- Dataset information and statistics
- Training progress
- Model accuracy (~99%)
- Feature importance rankings
- Model files saved in `models/` directory

**Files Created:**
- `models/rf_model.pkl` - Trained Random Forest model
- `models/scaler.pkl` - Feature scaler
- `models/label_encoder.pkl` - Label encoder
- `models/crop_info.json` - Crop metadata

### Step 3: Run the Web Application

```bash
python app.py
```

The server will start on `http://localhost:5000`

### Step 4: Access the Application

Open your web browser and go to:
```
http://localhost:5000
```

## Troubleshooting

### Issue: pip not found

**Solution:** Install pip first:
```bash
# For Ubuntu/Debian
sudo apt-get install python3-pip

# For macOS
brew install python3

# For Windows
# Download and install Python from python.org
```

### Issue: Module not found errors

**Solution:** Ensure all dependencies are installed:
```bash
pip install flask flask-cors pandas numpy scikit-learn joblib
```

### Issue: Port 5000 already in use

**Solution:** Change the port in `app.py`:
```python
# In app.py, last line:
app.run(debug=True, host='0.0.0.0', port=5001)  # Changed to 5001
```

### Issue: Model training fails

**Solution:** Verify the dataset exists:
```bash
ls data/Crop_recommendation.csv
```

If missing, ensure the CSV file is in the `data/` directory.

## Testing the Application

### Manual Testing

1. Enter sample values:
   - Nitrogen: 90
   - Phosphorus: 42
   - Potassium: 43
   - Temperature: 20.8
   - Humidity: 82
   - pH: 6.5
   - Rainfall: 202.9

2. Click "Get Crop Recommendation"

3. Expected result: Rice with ~98-99% confidence

### API Testing

Using curl:
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "nitrogen": 90,
    "phosphorus": 42,
    "potassium": 43,
    "temperature": 20.8,
    "humidity": 82,
    "ph": 6.5,
    "rainfall": 202.9
  }'
```

## System Requirements

- **Python**: 3.8 or higher
- **RAM**: Minimum 2GB
- **Storage**: 500MB free space
- **Browser**: Chrome, Firefox, Safari, or Edge (latest versions)
- **Internet**: Required for initial setup only

## Optional Features

### Voice Input

Voice input requires:
- Modern browser with Web Speech API support (Chrome recommended)
- Microphone permission granted
- Quiet environment for best results

### Multi-Language Support

Currently supports:
- English
- Hindi (हिंदी)
- Tamil (தமிழ்)

More languages can be added by editing `static/js/app.js`

## Development Mode

Run with auto-reload for development:
```python
# In app.py, set debug=True (already set by default)
app.run(debug=True, host='0.0.0.0', port=5000)
```

## Production Deployment

For production, use a WSGI server like Gunicorn:

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Next Steps

1. Train the model: `python model_training.py`
2. Start the app: `python app.py`
3. Open browser: `http://localhost:5000`
4. Test with sample data
5. Share with farmers!

## Support

For issues or questions:
- Check this setup guide
- Review the main README.md
- Test with the sample values provided above
