from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import json

app = Flask(__name__)
CORS(app)

# Load model, scaler, and label encoder
rf_model = joblib.load('models/rf_model.pkl')
scaler = joblib.load('models/scaler.pkl')
label_encoder = joblib.load('models/label_encoder.pkl')

# Load crop info
with open('models/crop_info.json', 'r') as f:
    crop_info = json.load(f)

# Crop descriptions and growing tips
CROP_DETAILS = {
    'rice': {
        'icon': '🌾',
        'description': 'Rice is a staple food crop requiring warm, humid conditions with plenty of water.',
        'tips': ['Ensure good water supply', 'Plant during monsoon', 'Maintain proper drainage'],
        'season': 'Kharif (Monsoon)',
        'duration': '4-5 months'
    },
    'maize': {
        'icon': '🌽',
        'description': 'Maize is a versatile cereal crop grown in various climates.',
        'tips': ['Needs well-drained soil', 'Moderate water required', 'Protect from pests'],
        'season': 'Kharif/Rabi',
        'duration': '3-4 months'
    },
    'chickpea': {
        'icon': '🫘',
        'description': 'Chickpea is a protein-rich pulse crop that thrives in cool, dry weather.',
        'tips': ['Plant in winter', 'Minimal irrigation needed', 'Good rotation crop'],
        'season': 'Rabi (Winter)',
        'duration': '4-5 months'
    },
    'kidneybeans': {
        'icon': '🫘',
        'description': 'Kidney beans are nutritious legumes requiring moderate temperatures.',
        'tips': ['Avoid waterlogging', 'Moderate temperature needed', 'Regular weeding important'],
        'season': 'Kharif',
        'duration': '3-4 months'
    },
    'pigeonpeas': {
        'icon': '🫛',
        'description': 'Pigeon peas are drought-resistant pulse crops.',
        'tips': ['Drought tolerant', 'Long duration crop', 'Good for dry regions'],
        'season': 'Kharif',
        'duration': '5-7 months'
    },
    'mothbeans': {
        'icon': '🫘',
        'description': 'Moth beans are highly drought-resistant legumes.',
        'tips': ['Excellent for arid zones', 'Minimal water needs', 'Heat tolerant'],
        'season': 'Kharif',
        'duration': '3 months'
    },
    'mungbean': {
        'icon': '🫛',
        'description': 'Mung beans are short-duration pulse crops.',
        'tips': ['Short growing period', 'Good summer crop', 'Nitrogen fixing'],
        'season': 'Summer/Kharif',
        'duration': '2-3 months'
    },
    'blackgram': {
        'icon': '⚫',
        'description': 'Black gram is a highly nutritious pulse crop.',
        'tips': ['Prefers warm weather', 'Good rotation crop', 'Moderate water needs'],
        'season': 'Kharif/Summer',
        'duration': '3-4 months'
    },
    'lentil': {
        'icon': '🫘',
        'description': 'Lentils are cool-season pulse crops rich in protein.',
        'tips': ['Cool weather preferred', 'Minimal irrigation', 'Winter season crop'],
        'season': 'Rabi (Winter)',
        'duration': '4-5 months'
    },
    'pomegranate': {
        'icon': '🍎',
        'description': 'Pomegranate is a fruit crop suited for semi-arid regions.',
        'tips': ['Drought resistant', 'Needs well-drained soil', 'Long-term investment'],
        'season': 'Year-round',
        'duration': 'Perennial'
    },
    'banana': {
        'icon': '🍌',
        'description': 'Banana requires warm climate and plenty of water.',
        'tips': ['High water requirement', 'Rich soil needed', 'Protect from wind'],
        'season': 'Year-round',
        'duration': '12-15 months'
    },
    'mango': {
        'icon': '🥭',
        'description': 'Mango is the king of fruits, requiring tropical climate.',
        'tips': ['Needs hot summer', 'Deep soil preferred', 'Long-term fruit crop'],
        'season': 'Year-round (fruits in summer)',
        'duration': 'Perennial'
    },
    'grapes': {
        'icon': '🍇',
        'description': 'Grapes are climbing vines requiring specific conditions.',
        'tips': ['Needs support structure', 'Pruning essential', 'Good market value'],
        'season': 'Year-round',
        'duration': 'Perennial'
    },
    'watermelon': {
        'icon': '🍉',
        'description': 'Watermelon is a summer fruit requiring warm weather.',
        'tips': ['Hot weather needed', 'Plenty of space required', 'Good water supply'],
        'season': 'Summer',
        'duration': '3-4 months'
    },
    'muskmelon': {
        'icon': '🍈',
        'description': 'Muskmelon is a sweet summer fruit.',
        'tips': ['Warm season crop', 'Well-drained soil', 'Regular irrigation'],
        'season': 'Summer',
        'duration': '3 months'
    },
    'apple': {
        'icon': '🍎',
        'description': 'Apples require cool climate and are grown in hilly regions.',
        'tips': ['Cool climate essential', 'Hilly areas preferred', 'Winter chilling needed'],
        'season': 'Year-round (fruits in autumn)',
        'duration': 'Perennial'
    },
    'orange': {
        'icon': '🍊',
        'description': 'Oranges are citrus fruits requiring specific conditions.',
        'tips': ['Subtropical climate', 'Good drainage needed', 'Regular pruning'],
        'season': 'Year-round',
        'duration': 'Perennial'
    },
    'papaya': {
        'icon': '🍈',
        'description': 'Papaya is a fast-growing tropical fruit.',
        'tips': ['Tropical climate', 'Quick growing', 'Regular watering'],
        'season': 'Year-round',
        'duration': '10-12 months'
    },
    'coconut': {
        'icon': '🥥',
        'description': 'Coconut is a versatile palm tree crop for coastal areas.',
        'tips': ['Coastal areas ideal', 'High water table', 'Long-term crop'],
        'season': 'Year-round',
        'duration': 'Perennial'
    },
    'cotton': {
        'icon': '☁️',
        'description': 'Cotton is a major fiber crop requiring warm climate.',
        'tips': ['Warm weather needed', 'Deep black soil preferred', 'Pest management crucial'],
        'season': 'Kharif',
        'duration': '5-6 months'
    },
    'jute': {
        'icon': '🌿',
        'description': 'Jute is a fiber crop requiring high humidity and rainfall.',
        'tips': ['High humidity needed', 'Waterlogged areas suitable', 'Retting process required'],
        'season': 'Kharif',
        'duration': '4-5 months'
    },
    'coffee': {
        'icon': '☕',
        'description': 'Coffee is a plantation crop requiring shade and moderate climate.',
        'tips': ['Shade required', 'Hilly terrain ideal', 'Specific altitude needed'],
        'season': 'Year-round',
        'duration': 'Perennial'
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        # Extract features in correct order
        features = np.array([[
            float(data['nitrogen']),
            float(data['phosphorus']),
            float(data['potassium']),
            float(data['temperature']),
            float(data['humidity']),
            float(data['ph']),
            float(data['rainfall'])
        ]])

        # Scale features
        features_scaled = scaler.transform(features)

        # Get prediction and probabilities
        prediction = rf_model.predict(features_scaled)
        probabilities = rf_model.predict_proba(features_scaled)[0]

        # Get crop name
        crop = label_encoder.inverse_transform(prediction)[0]

        # Get top 3 recommendations
        top_3_indices = np.argsort(probabilities)[-3:][::-1]
        recommendations = []

        for idx in top_3_indices:
            crop_name = label_encoder.inverse_transform([idx])[0]
            confidence = float(probabilities[idx] * 100)

            crop_detail = CROP_DETAILS.get(crop_name, {
                'icon': '🌱',
                'description': f'{crop_name.title()} crop',
                'tips': ['Consult local agricultural expert'],
                'season': 'Varies',
                'duration': 'Varies'
            })

            recommendations.append({
                'crop': crop_name,
                'confidence': round(confidence, 2),
                'icon': crop_detail['icon'],
                'description': crop_detail['description'],
                'tips': crop_detail['tips'],
                'season': crop_detail['season'],
                'duration': crop_detail['duration']
            })

        return jsonify({
            'success': True,
            'primary_crop': crop,
            'recommendations': recommendations,
            'input_data': {
                'nitrogen': data['nitrogen'],
                'phosphorus': data['phosphorus'],
                'potassium': data['potassium'],
                'temperature': data['temperature'],
                'humidity': data['humidity'],
                'ph': data['ph'],
                'rainfall': data['rainfall']
            }
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/crops', methods=['GET'])
def get_crops():
    return jsonify({
        'crops': crop_info['crops'],
        'total': len(crop_info['crops'])
    })

@app.route('/api/feature-importance', methods=['GET'])
def get_feature_importance():
    return jsonify(crop_info['feature_importance'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
