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
    print(" Error: 'Crop_recommendation.csv' not found! Please put the file in this folder.")
    exit()

df = pd.read_csv("Crop_recommendation.csv")


X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']


model_dir = "backend/model"
os.makedirs(model_dir, exist_ok=True)


label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
pickle.dump(label_encoder, open(os.path.join(model_dir, "label_encoder.pkl"), "wb"))


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pickle.dump(scaler, open(os.path.join(model_dir, "scaler.pkl"), "wb"))

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_encoded, test_size=0.2, random_state=42
)


model = Sequential([
    Input(shape=(7,)),                  
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(len(label_encoder.classes_), activation='softmax')
])


model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)


print("Training ANN Model...")
model.fit(X_train, y_train, epochs=50, batch_size=16, verbose=1)


loss, accuracy = model.evaluate(X_test, y_test)
print(f" Model Accuracy: {accuracy * 100:.2f}%")


model.save(os.path.join(model_dir, "crop_model_ann.keras"))
print(" ANN Model Saved Successfully (Keras format) inside 'backend/model' folder!")
