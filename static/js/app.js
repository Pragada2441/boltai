// Multi-language support
const translations = {
    en: {
        'voice-title': '🎤 Voice Input Available',
        'voice-subtitle': 'Speak your soil and weather details',
        'start-voice': 'Start Voice Input',
        'form-title': '📝 Enter Your Field Details',
        'nitrogen': 'Nitrogen (N)',
        'nitrogen-help': 'Typical range: 0-200 kg/ha',
        'phosphorus': 'Phosphorus (P)',
        'phosphorus-help': 'Typical range: 0-200 kg/ha',
        'potassium': 'Potassium (K)',
        'potassium-help': 'Typical range: 0-250 kg/ha',
        'temperature': 'Temperature (°C)',
        'temperature-help': 'Average temperature in Celsius',
        'humidity': 'Humidity (%)',
        'humidity-help': 'Relative humidity percentage',
        'ph': 'Soil pH',
        'ph-help': 'Soil pH value (3-10, neutral is 7)',
        'rainfall': 'Rainfall (mm)',
        'rainfall-help': 'Annual rainfall in millimeters',
        'get-recommendation': '🌱 Get Crop Recommendation',
        'results-title': '🎯 Recommended Crops for Your Field',
        'analyzing': 'Analyzing your field data...'
    },
    hi: {
        'voice-title': '🎤 आवाज इनपुट उपलब्ध',
        'voice-subtitle': 'अपनी मिट्टी और मौसम की जानकारी बोलें',
        'start-voice': 'आवाज इनपुट शुरू करें',
        'form-title': '📝 अपने खेत का विवरण दर्ज करें',
        'nitrogen': 'नाइट्रोजन (N)',
        'nitrogen-help': 'सामान्य सीमा: 0-200 किलो/हेक्टेयर',
        'phosphorus': 'फास्फोरस (P)',
        'phosphorus-help': 'सामान्य सीमा: 0-200 किलो/हेक्टेयर',
        'potassium': 'पोटैशियम (K)',
        'potassium-help': 'सामान्य सीमा: 0-250 किलो/हेक्टेयर',
        'temperature': 'तापमान (°C)',
        'temperature-help': 'सेल्सियस में औसत तापमान',
        'humidity': 'आर्द्रता (%)',
        'humidity-help': 'सापेक्ष आर्द्रता प्रतिशत',
        'ph': 'मिट्टी का pH',
        'ph-help': 'मिट्टी का pH मान (3-10, तटस्थ 7 है)',
        'rainfall': 'वर्षा (मिमी)',
        'rainfall-help': 'वार्षिक वर्षा मिलीमीटर में',
        'get-recommendation': '🌱 फसल सिफारिश प्राप्त करें',
        'results-title': '🎯 आपके खेत के लिए अनुशंसित फसलें',
        'analyzing': 'आपके खेत के डेटा का विश्लेषण कर रहे हैं...'
    },
    ta: {
        'voice-title': '🎤 குரல் உள்ளீடு கிடைக்கிறது',
        'voice-subtitle': 'உங்கள் மண் மற்றும் வானிலை விவரங்களைப் பேசுங்கள்',
        'start-voice': 'குரல் உள்ளீட்டைத் தொடங்கவும்',
        'form-title': '📝 உங்கள் வயல் விவரங்களை உள்ளிடவும்',
        'nitrogen': 'நைட்ரஜன் (N)',
        'nitrogen-help': 'வழக்கமான வரம்பு: 0-200 கிலோ/ஹெக்டேர்',
        'phosphorus': 'பாஸ்பரஸ் (P)',
        'phosphorus-help': 'வழக்கமான வரம்பு: 0-200 கிலோ/ஹெக்டேர்',
        'potassium': 'பொட்டாசியம் (K)',
        'potassium-help': 'வழக்கமான வரம்பு: 0-250 கிலோ/ஹெக்டேர்',
        'temperature': 'வெப்பநிலை (°C)',
        'temperature-help': 'சராசரி வெப்பநிலை செல்சியஸில்',
        'humidity': 'ஈரப்பதம் (%)',
        'humidity-help': 'ஒப்பீட்டு ஈரப்பதம் சதவீதம்',
        'ph': 'மண் pH',
        'ph-help': 'மண் pH மதிப்பு (3-10, நடுநிலை 7)',
        'rainfall': 'மழைப்பொழிவு (மிமீ)',
        'rainfall-help': 'ஆண்டு மழைப்பொழிவு மில்லிமீட்டரில்',
        'get-recommendation': '🌱 பயிர் பரிந்துரையைப் பெறுங்கள்',
        'results-title': '🎯 உங்கள் வயலுக்கு பரிந்துரைக்கப்பட்ட பயிர்கள்',
        'analyzing': 'உங்கள் வயல் தரவை பகுப்பாய்வு செய்கிறது...'
    }
};

let currentLang = 'en';

// Language switcher
document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentLang = btn.dataset.lang;
        updateLanguage();
    });
});

function updateLanguage() {
    document.querySelectorAll('[data-translate]').forEach(element => {
        const key = element.getAttribute('data-translate');
        if (translations[currentLang][key]) {
            element.textContent = translations[currentLang][key];
        }
    });
}

// Visual feedback for inputs
const inputs = ['nitrogen', 'phosphorus', 'potassium', 'temperature', 'humidity', 'ph', 'rainfall'];
const maxValues = {
    nitrogen: 200,
    phosphorus: 200,
    potassium: 250,
    temperature: 50,
    humidity: 100,
    ph: 14,
    rainfall: 500
};

inputs.forEach(inputId => {
    const input = document.getElementById(inputId);
    const bar = document.getElementById(`${inputId}-bar`);

    input.addEventListener('input', () => {
        const value = parseFloat(input.value) || 0;
        const max = maxValues[inputId];
        const percentage = Math.min((value / max) * 100, 100);
        bar.style.width = `${percentage}%`;
    });
});

// Voice input (Web Speech API)
const voiceBtn = document.getElementById('voiceBtn');
const voiceStatus = document.getElementById('voiceStatus');

if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = false;

    let isListening = false;

    voiceBtn.addEventListener('click', () => {
        if (!isListening) {
            recognition.start();
            isListening = true;
            voiceBtn.style.background = 'linear-gradient(135deg, #e74c3c 0%, #c0392b 100%)';
            voiceStatus.textContent = 'Listening... Speak now!';
        } else {
            recognition.stop();
            isListening = false;
            voiceBtn.style.background = 'linear-gradient(135deg, #3498db 0%, #2980b9 100%)';
            voiceStatus.textContent = '';
        }
    });

    recognition.onresult = (event) => {
        const transcript = event.results[event.results.length - 1][0].transcript.toLowerCase();
        voiceStatus.textContent = `Heard: "${transcript}"`;

        // Parse voice input (simple keyword matching)
        const words = transcript.split(' ');
        words.forEach((word, index) => {
            const number = parseFloat(words[index + 1]);
            if (!isNaN(number)) {
                if (word.includes('nitrogen')) document.getElementById('nitrogen').value = number;
                if (word.includes('phosphorus') || word.includes('phosphor')) document.getElementById('phosphorus').value = number;
                if (word.includes('potassium') || word.includes('potash')) document.getElementById('potassium').value = number;
                if (word.includes('temperature') || word.includes('temp')) document.getElementById('temperature').value = number;
                if (word.includes('humidity')) document.getElementById('humidity').value = number;
                if (word.includes('ph') || word.includes('acidity')) document.getElementById('ph').value = number;
                if (word.includes('rainfall') || word.includes('rain')) document.getElementById('rainfall').value = number;
            }
        });

        // Trigger input events to update visual bars
        inputs.forEach(inputId => {
            const input = document.getElementById(inputId);
            input.dispatchEvent(new Event('input'));
        });
    };

    recognition.onerror = (event) => {
        voiceStatus.textContent = `Error: ${event.error}`;
        isListening = false;
    };
} else {
    voiceBtn.disabled = true;
    voiceStatus.textContent = 'Voice input not supported in this browser';
}

// Form submission
const cropForm = document.getElementById('cropForm');
const loadingOverlay = document.getElementById('loadingOverlay');
const resultsSection = document.getElementById('resultsSection');
const resultsContainer = document.getElementById('resultsContainer');

cropForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = {
        nitrogen: parseFloat(document.getElementById('nitrogen').value),
        phosphorus: parseFloat(document.getElementById('phosphorus').value),
        potassium: parseFloat(document.getElementById('potassium').value),
        temperature: parseFloat(document.getElementById('temperature').value),
        humidity: parseFloat(document.getElementById('humidity').value),
        ph: parseFloat(document.getElementById('ph').value),
        rainfall: parseFloat(document.getElementById('rainfall').value)
    };

    // Show loading
    loadingOverlay.classList.add('active');

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();

        if (data.success) {
            displayResults(data);
            resultsSection.style.display = 'block';
            resultsSection.scrollIntoView({ behavior: 'smooth' });
        } else {
            alert('Error: ' + data.error);
        }
    } catch (error) {
        alert('Error connecting to server: ' + error.message);
    } finally {
        loadingOverlay.classList.remove('active');
    }
});

function displayResults(data) {
    resultsContainer.innerHTML = '';

    data.recommendations.forEach((rec, index) => {
        const isPrimary = index === 0;
        const card = document.createElement('div');
        card.className = `crop-card ${isPrimary ? 'primary' : ''}`;

        card.innerHTML = `
            <div class="crop-header">
                <div class="crop-title">
                    <span class="crop-icon">${rec.icon}</span>
                    <div>
                        <h3>${rec.crop}</h3>
                        ${isPrimary ? '<span style="color: #f39c12; font-size: 14px;">⭐ Best Match</span>' : ''}
                    </div>
                </div>
                <div class="confidence-badge">${rec.confidence.toFixed(1)}% Match</div>
            </div>
            <p class="crop-description">${rec.description}</p>
            <div class="crop-info">
                <div class="info-item">
                    <strong>🗓️ Season</strong>
                    <span>${rec.season}</span>
                </div>
                <div class="info-item">
                    <strong>⏱️ Duration</strong>
                    <span>${rec.duration}</span>
                </div>
            </div>
            <div class="crop-tips">
                <h4>💡 Growing Tips:</h4>
                <ul>
                    ${rec.tips.map(tip => `<li>${tip}</li>`).join('')}
                </ul>
            </div>
        `;

        resultsContainer.appendChild(card);
    });
}

// Smooth scroll for better UX
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Add ripple effect to buttons
function createRipple(event) {
    const button = event.currentTarget;
    const ripple = document.createElement('span');
    const diameter = Math.max(button.clientWidth, button.clientHeight);
    const radius = diameter / 2;

    ripple.style.width = ripple.style.height = `${diameter}px`;
    ripple.style.left = `${event.clientX - button.offsetLeft - radius}px`;
    ripple.style.top = `${event.clientY - button.offsetTop - radius}px`;
    ripple.classList.add('ripple');

    button.appendChild(ripple);

    setTimeout(() => ripple.remove(), 600);
}

document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', createRipple);
});
