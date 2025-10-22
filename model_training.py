import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib
import json

# Load dataset
df = pd.read_csv('data/Crop_recommendation.csv')

# Basic info
print("Dataset shape:", df.shape)
print("\nDataset columns:", df.columns.tolist())
print("\nCrop distribution:")
print(df['label'].value_counts())
print("\nDataset info:")
print(df.info())
print("\nMissing values:")
print(df.isnull().sum())

# Prepare features and target
X = df.drop('label', axis=1)
y = df['label']

# Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split data (70-30 split like R model)
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.3, random_state=123, stratify=y_encoded
)

# Scale features (center and scale like R model)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Random Forest model with same parameters as R
# mtry = floor(sqrt(7)) = 2
rf_model = RandomForestClassifier(
    n_estimators=1000,
    max_features='sqrt',  # equivalent to mtry parameter
    random_state=123,
    n_jobs=-1,
    verbose=1
)

print("\nTraining Random Forest model...")
rf_model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = rf_model.predict(X_test_scaled)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f"\n{'='*50}")
print(f"Model Accuracy: {accuracy*100:.2f}%")
print(f"{'='*50}")

# Detailed classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# Confusion matrix
print("\nConfusion Matrix:")
conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)

# Feature importance
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

print("\nFeature Importance:")
print(feature_importance)

# Save model, scaler, and label encoder
joblib.dump(rf_model, 'models/rf_model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')
joblib.dump(label_encoder, 'models/label_encoder.pkl')

# Save feature importance and crop info
crop_info = {
    'crops': label_encoder.classes_.tolist(),
    'features': X.columns.tolist(),
    'feature_importance': feature_importance.to_dict('records')
}

with open('models/crop_info.json', 'w') as f:
    json.dump(crop_info, f, indent=2)

print("\n✓ Model, scaler, and metadata saved successfully!")
print(f"✓ Model accuracy: {accuracy*100:.2f}%")
