# AgriSense System Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                      AGRISENSE SYSTEM                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │         USER INTERFACE (Frontend)       │
        │  • Voice Input (Web Speech API)         │
        │  • Visual Form with Feedback            │
        │  • Multi-Language Support               │
        │  • Responsive Design                    │
        └─────────────────────────────────────────┘
                              │
                              ▼ HTTP/JSON
        ┌─────────────────────────────────────────┐
        │        FLASK API (Backend)              │
        │  • POST /predict                        │
        │  • GET /api/crops                       │
        │  • GET /api/feature-importance          │
        └─────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │      ML MODEL (Random Forest)           │
        │  • 1000 Decision Trees                  │
        │  • 7 Features Input                     │
        │  • 22 Crop Classes Output               │
        │  • ~99% Accuracy                        │
        └─────────────────────────────────────────┘
```

## Data Flow

```
1. FARMER INPUT
   ├─ Manual Entry (Form)
   │  └─ N, P, K, Temp, Humidity, pH, Rainfall
   │
   └─ Voice Input (Speech API)
      └─ Spoken values converted to numbers

                    ↓

2. FRONTEND VALIDATION
   ├─ Range Checking
   ├─ Visual Feedback
   └─ Form Completion Check

                    ↓

3. API REQUEST (JSON)
   {
     "nitrogen": 90,
     "phosphorus": 42,
     "potassium": 43,
     "temperature": 20.8,
     "humidity": 82,
     "ph": 6.5,
     "rainfall": 202.9
   }

                    ↓

4. BACKEND PROCESSING
   ├─ Data Validation
   ├─ Feature Scaling (StandardScaler)
   └─ Model Prediction

                    ↓

5. ML MODEL
   ├─ Random Forest Classification
   ├─ Probability Calculation
   └─ Top 3 Crops Selection

                    ↓

6. API RESPONSE (JSON)
   {
     "success": true,
     "primary_crop": "rice",
     "recommendations": [
       {
         "crop": "rice",
         "confidence": 98.5,
         "icon": "🌾",
         "description": "...",
         "tips": [...],
         "season": "Kharif",
         "duration": "4-5 months"
       },
       ...
     ]
   }

                    ↓

7. RESULTS DISPLAY
   ├─ Visual Crop Cards
   ├─ Confidence Badges
   ├─ Growing Tips
   └─ Season Information
```

## Component Architecture

### 1. Frontend Layer

```
┌─────────────────────────────────────────────────────────────┐
│                    templates/index.html                     │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  Header                                               │  │
│  │  • Logo & Title                                       │  │
│  │  • Language Selector                                  │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  Voice Input Section                                  │  │
│  │  • Microphone Button                                  │  │
│  │  • Status Display                                     │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  Input Form                                           │  │
│  │  • 7 Input Fields with Icons                         │  │
│  │  • Visual Progress Bars                              │  │
│  │  • Help Text                                          │  │
│  │  • Submit Button                                      │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  Results Section (Dynamic)                           │  │
│  │  • Top 3 Crop Cards                                   │  │
│  │  • Confidence Scores                                  │  │
│  │  • Growing Information                                │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  Education Section                                    │  │
│  │  • Soil Health Info                                   │  │
│  │  • Climate Info                                       │  │
│  │  • Best Practices                                     │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘

         Styled by: static/css/style.css
         Logic in: static/js/app.js
```

### 2. Backend Layer

```
┌─────────────────────────────────────────────────────────────┐
│                         app.py                              │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Flask Application                                     │ │
│  │  • CORS enabled                                        │ │
│  │  • Route handlers                                      │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Model Loader                                          │ │
│  │  • Load rf_model.pkl                                   │ │
│  │  • Load scaler.pkl                                     │ │
│  │  • Load label_encoder.pkl                              │ │
│  │  • Load crop_info.json                                 │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Prediction Pipeline                                   │ │
│  │  1. Validate input                                     │ │
│  │  2. Scale features                                     │ │
│  │  3. Get predictions                                    │ │
│  │  4. Calculate probabilities                            │ │
│  │  5. Rank crops                                         │ │
│  │  6. Add crop details                                   │ │
│  │  7. Return JSON response                               │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Crop Details Database                                 │ │
│  │  • 22 crops with metadata                              │ │
│  │  • Icons, descriptions, tips                           │ │
│  │  • Season & duration info                              │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### 3. Machine Learning Layer

```
┌─────────────────────────────────────────────────────────────┐
│                   model_training.py                         │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Data Loading & Preprocessing                          │ │
│  │  • Read CSV (2200+ samples)                            │ │
│  │  • Feature engineering                                 │ │
│  │  • Label encoding                                      │ │
│  └────────────────────────────────────────────────────────┘ │
│                          ↓                                  │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Train-Test Split (70-30)                              │ │
│  └────────────────────────────────────────────────────────┘ │
│                          ↓                                  │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Feature Scaling                                       │ │
│  │  • StandardScaler (center & scale)                     │ │
│  └────────────────────────────────────────────────────────┘ │
│                          ↓                                  │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Random Forest Training                                │ │
│  │  • n_estimators: 1000                                  │ │
│  │  • max_features: sqrt                                  │ │
│  │  • random_state: 123                                   │ │
│  └────────────────────────────────────────────────────────┘ │
│                          ↓                                  │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Model Evaluation                                      │ │
│  │  • Accuracy: ~99%                                      │ │
│  │  • Confusion matrix                                    │ │
│  │  • Classification report                               │ │
│  │  • Feature importance                                  │ │
│  └────────────────────────────────────────────────────────┘ │
│                          ↓                                  │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Save Models                                           │ │
│  │  • rf_model.pkl                                        │ │
│  │  • scaler.pkl                                          │ │
│  │  • label_encoder.pkl                                   │ │
│  │  • crop_info.json                                      │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Technology Stack

```
┌───────────────────────────────────────────────────────┐
│                   FRONTEND                            │
│  • HTML5 - Semantic structure                         │
│  • CSS3 - Modern styling, animations                  │
│  • JavaScript ES6+ - Interactive features             │
│  • Web Speech API - Voice input                       │
└───────────────────────────────────────────────────────┘
                         │
                         │ HTTP/JSON
                         ▼
┌───────────────────────────────────────────────────────┐
│                   BACKEND                             │
│  • Flask 3.0 - Web framework                          │
│  • Flask-CORS - Cross-origin requests                 │
│  • Python 3.8+ - Programming language                 │
└───────────────────────────────────────────────────────┘
                         │
                         ▼
┌───────────────────────────────────────────────────────┐
│              MACHINE LEARNING                         │
│  • scikit-learn - ML framework                        │
│  • pandas - Data manipulation                         │
│  • NumPy - Numerical computing                        │
│  • joblib - Model serialization                       │
└───────────────────────────────────────────────────────┘
```

## Deployment Architecture

```
                    ┌──────────────┐
                    │   Internet   │
                    └──────────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  Web Server  │
                    │  (Gunicorn)  │
                    └──────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │   Flask Application    │
              │   • Route handlers     │
              │   • Business logic     │
              └────────────────────────┘
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
      ┌──────────────┐        ┌──────────────┐
      │  Static Files│        │  ML Models   │
      │  • HTML      │        │  • .pkl files│
      │  • CSS       │        │  • .json     │
      │  • JS        │        └──────────────┘
      └──────────────┘
```

## Security Considerations

```
┌─────────────────────────────────────────────────────┐
│  INPUT VALIDATION                                   │
│  • Type checking (numbers only)                     │
│  • Range validation (min/max values)                │
│  • Sanitization of user input                       │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  API SECURITY                                       │
│  • CORS configuration                               │
│  • Error handling (no stack traces exposed)         │
│  • Rate limiting (can be added)                     │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  DATA PRIVACY                                       │
│  • No data storage (stateless)                      │
│  • No user tracking                                 │
│  • No personal information collected                │
└─────────────────────────────────────────────────────┘
```

## Performance Optimization

```
┌─────────────────────────────────────────────────────┐
│  FRONTEND                                           │
│  • Minified CSS/JS (production)                     │
│  • Lazy loading of images                           │
│  • Browser caching                                  │
│  • Responsive images                                │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  BACKEND                                            │
│  • Model loaded once at startup                     │
│  • Efficient NumPy operations                       │
│  • JSON responses (lightweight)                     │
│  • Async support (can be added)                     │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  MODEL                                              │
│  • Pre-trained (no training overhead)               │
│  • Fast prediction (<100ms)                         │
│  • Optimized Random Forest                          │
└─────────────────────────────────────────────────────┘
```

## Scalability

```
Current Setup (Single Server):
  ├─ Handles: ~100 concurrent users
  ├─ Response time: <1 second
  └─ Resource usage: Low

Future Scaling Options:
  ├─ Load Balancer
  │   └─ Multiple Flask instances
  ├─ Caching Layer (Redis)
  │   └─ Cache frequent predictions
  ├─ CDN for Static Files
  │   └─ Faster global delivery
  └─ Database (Optional)
      └─ Store user history/analytics
```

## Monitoring & Logging

```
Recommended Setup:
  ├─ Application Logs
  │   ├─ Request/response times
  │   ├─ Error tracking
  │   └─ Usage statistics
  │
  ├─ Health Checks
  │   ├─ API availability
  │   ├─ Model status
  │   └─ Resource usage
  │
  └─ Analytics
      ├─ Popular crops
      ├─ User demographics
      └─ Prediction accuracy feedback
```

## Development vs Production

```
DEVELOPMENT MODE:
  • Debug enabled
  • Auto-reload on code changes
  • Detailed error messages
  • Single threaded
  • Command: python app.py

PRODUCTION MODE:
  • Debug disabled
  • Gunicorn WSGI server
  • Error logging only
  • Multi-threaded/workers
  • Command: gunicorn -w 4 app:app
```

This architecture ensures AgriSense is scalable, maintainable, and production-ready!
