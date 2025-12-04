import pandas as pd
import numpy as np
import pickle
import os
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from keras.models import Sequential
from keras.layers import Dense, Input


if not os.path.exists("Crop_recommendation.csv"):
    print("Error: 'Crop_recommendation.csv' not found!")
    exit()

df = pd.read_csv("Crop_recommendation.csv")


X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']


label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)


model = Sequential([
    Input(shape=(7,)),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(len(label_encoder.classes_), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


print("Training ANN model...")
model.fit(X_train, y_train, epochs=50, batch_size=16, verbose=1)


loss, accuracy = model.evaluate(X_test, y_test)
print(f"Model Accuracy: {accuracy*100:.2f}%")


os.makedirs("model", exist_ok=True)
model.save("model/crop_model_ann.keras")
pickle.dump(scaler, open("model/scaler.pkl", "wb"))
pickle.dump(label_encoder, open("model/label_encoder.pkl", "wb"))
print("Model, scaler & encoder saved in 'model/' folder!")




print("\nEnter feature values for prediction:")
N = float(input("N (Nitrogen): "))
P = float(input("P (Phosphorus): "))
K = float(input("K (Potassium): "))
temperature = float(input("Temperature (°C): "))
humidity = float(input("Humidity (%): "))
ph = float(input("Soil pH: "))
rainfall = float(input("Rainfall (mm): "))


features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
features_scaled = scaler.transform(features)


pred_probs = model.predict(features_scaled)
pred_index = np.argmax(pred_probs, axis=1)[0]
recommended_crop = label_encoder.inverse_transform([pred_index])[0]

print(f"\nRecommended Crop: {recommended_crop}")
