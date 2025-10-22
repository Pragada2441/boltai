# AgriSense: AI-Based Crop Recommendation System

AgriSense is an intelligent crop recommendation system designed to help farmers make data-driven decisions about which crops to grow based on soil conditions and environmental factors.

## Features

### 🌟 Core Features
- **AI-Powered Recommendations**: Uses Random Forest ML model trained on 2200+ data points
- **Multi-Crop Support**: Recommends from 22 different crop types
- **Confidence Scoring**: Provides top 3 crop recommendations with confidence percentages
- **Real-time Prediction**: Instant crop recommendations based on input parameters

### 🎯 User-Friendly Design
- **Accessible Interface**: Designed for both literate and illiterate farmers
- **Visual Feedback**: Interactive input bars showing data ranges
- **Voice Input**: Speech recognition for hands-free data entry
- **Multi-Language Support**: English, Hindi, and Tamil translations
- **Mobile Responsive**: Works seamlessly on phones, tablets, and desktops

### 📊 Input Parameters
The system analyzes 7 key factors:
1. **Nitrogen (N)**: Soil nitrogen content (0-200 kg/ha)
2. **Phosphorus (P)**: Soil phosphorus content (0-200 kg/ha)
3. **Potassium (K)**: Soil potassium content (0-250 kg/ha)
4. **Temperature**: Average temperature (°C)
5. **Humidity**: Relative humidity (%)
6. **pH**: Soil pH level (3-10)
7. **Rainfall**: Annual rainfall (mm)

### 🌾 Supported Crops
- Cereals: Rice, Maize
- Pulses: Chickpea, Kidney Beans, Pigeon Peas, Moth Beans, Mung Bean, Black Gram, Lentil
- Fruits: Pomegranate, Banana, Mango, Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, Coconut
- Cash Crops: Cotton, Jute, Coffee

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Train the model**
```bash
python model_training.py
```

This will:
- Load and process the dataset
- Train the Random Forest model
- Generate evaluation metrics
- Save the trained model, scaler, and label encoder

3. **Run the application**
```bash
python app.py
```

4. **Access the application**
Open your browser and navigate to:
```
http://localhost:5000
```

## Model Performance

The Random Forest model achieves:
- **High Accuracy**: ~99% on test set (similar to R model)
- **Robust Predictions**: 1000 decision trees for stable results
- **Feature Importance**: Identifies key factors for each crop

### Model Architecture
- Algorithm: Random Forest Classifier
- Trees: 1000
- Max Features: sqrt (auto-tuned)
- Preprocessing: StandardScaler (center and scale)
- Train/Test Split: 70/30

## API Endpoints

### POST /predict
Get crop recommendations based on soil and weather data.

**Request Body:**
```json
{
  "nitrogen": 90,
  "phosphorus": 42,
  "potassium": 43,
  "temperature": 20.8,
  "humidity": 82.0,
  "ph": 6.5,
  "rainfall": 202.9
}
```

**Response:**
```json
{
  "success": true,
  "primary_crop": "rice",
  "recommendations": [
    {
      "crop": "rice",
      "confidence": 98.5,
      "icon": "🌾",
      "description": "Rice is a staple food crop...",
      "tips": ["Ensure good water supply", "..."],
      "season": "Kharif (Monsoon)",
      "duration": "4-5 months"
    }
  ]
}
```

### GET /api/crops
Get list of all supported crops.

### GET /api/feature-importance
Get feature importance rankings.

## Usage Guide

### For Literate Farmers
1. Select your preferred language (English, Hindi, or Tamil)
2. Enter soil test values (N, P, K, pH)
3. Input local weather conditions (temperature, humidity, rainfall)
4. Click "Get Crop Recommendation"
5. Review top 3 recommended crops with confidence scores
6. Read growing tips and season information

### For Illiterate Farmers
1. Use the voice input feature (🎙️ button)
2. Speak the values in your language
3. Visual bars show if values are in normal range
4. Large icons and emojis make results easy to understand
5. Get help from family members or agricultural extension workers

## Technology Stack

### Backend
- **Flask**: Web framework
- **scikit-learn**: Machine learning
- **pandas**: Data processing
- **NumPy**: Numerical computations

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with gradients and animations
- **JavaScript**: Interactive features and Web Speech API
- **Responsive Design**: Mobile-first approach

## Project Structure
```
project/
├── app.py                  # Flask application
├── model_training.py       # Model training script
├── requirements.txt        # Python dependencies
├── data/
│   └── Crop_recommendation.csv
├── models/
│   ├── rf_model.pkl       # Trained model
│   ├── scaler.pkl         # Feature scaler
│   ├── label_encoder.pkl  # Label encoder
│   └── crop_info.json     # Crop metadata
├── templates/
│   └── index.html         # Main HTML template
└── static/
    ├── css/
    │   └── style.css      # Styles
    └── js/
        └── app.js         # JavaScript logic
```

## Comparison with R Model

Both Python and R implementations achieve similar accuracy (~99%). The Python version offers:
- Easier deployment as web application
- Better integration with frontend
- More accessible API structure
- Production-ready Flask framework

## Future Enhancements

- Add weather API integration for automatic data fetching
- Include market price predictions
- Add crop disease detection
- Implement user accounts for saving recommendations
- Add SMS/WhatsApp notifications
- Include regional language support (more Indian languages)
- Add offline mobile app version
- Integrate with government agricultural schemes

---

**Made with ❤️ for Farmers**

*Empowering agriculture through AI technology*