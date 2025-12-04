import pickle
import numpy as np
import time

# Load trained model
model_path = "model/crop_model.pkl"  # নিশ্চিত হও model folder e আছে
model = pickle.load(open(model_path, "rb"))

def bot_print(msg):
    for char in msg:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

bot_print("🤖 Hi! I am your Crop Recommendation Bot.")
bot_print("Please answer a few questions about your farm conditions.\n")

# Collect inputs
def get_input(feature_name, unit=""):
    while True:
        try:
            value = float(input(f"{feature_name} ({unit}): "))
            return value
        except ValueError:
            bot_print("⚠️  Please enter a valid number.")

N = get_input("Nitrogen (N)", "kg/ha")
P = get_input("Phosphorus (P)", "kg/ha")
K = get_input("Potassium (K)", "kg/ha")
temperature = get_input("Temperature", "°C")
humidity = get_input("Humidity", "%")
ph = get_input("Soil pH")
rainfall = get_input("Rainfall", "mm")

bot_print("\nAnalyzing your inputs...")
time.sleep(1)  # small delay to simulate thinking

# Prepare features
features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

# Predict
predicted_crop = model.predict(features)

bot_print(f"\n🌱 Recommended Crop: {predicted_crop[0]}")
bot_print("Good luck with your farming! 🚜")
