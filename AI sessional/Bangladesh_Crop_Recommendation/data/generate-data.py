import pandas as pd
import random

# ডামি ডেটা তৈরির জন্য কিছু ফসলের রেঞ্জ
crops_data = {
    'rice': {'N': (60, 90), 'P': (35, 60), 'K': (35, 45), 'temp': (20, 27), 'hum': (80, 90), 'ph': (6, 7), 'rain': (180, 300)},
    'maize': {'N': (60, 100), 'P': (40, 60), 'K': (15, 25), 'temp': (18, 27), 'hum': (50, 70), 'ph': (5.5, 7), 'rain': (60, 100)},
    'jute': {'N': (60, 90), 'P': (35, 55), 'K': (35, 45), 'temp': (23, 28), 'hum': (70, 85), 'ph': (6, 7.5), 'rain': (150, 200)},
    'coffee': {'N': (80, 120), 'P': (15, 35), 'K': (25, 35), 'temp': (23, 28), 'hum': (50, 70), 'ph': (6, 8), 'rain': (110, 180)},
    'watermelon': {'N': (80, 120), 'P': (5, 30), 'K': (45, 55), 'temp': (24, 29), 'hum': (80, 90), 'ph': (6, 7), 'rain': (40, 60)},
}

data = []
# প্রতিটি ফসলের জন্য ১০০টি করে স্যাম্পল তৈরি হবে
for crop, ranges in crops_data.items():
    for _ in range(100): 
        row = {
            'N': random.randint(*ranges['N']),
            'P': random.randint(*ranges['P']),
            'K': random.randint(*ranges['K']),
            'temperature': random.uniform(*ranges['temp']),
            'humidity': random.uniform(*ranges['hum']),
            'ph': random.uniform(*ranges['ph']),
            'rainfall': random.uniform(*ranges['rain']),
            'label': crop
        }
        data.append(row)

# CSV ফাইল হিসেবে সেভ করা
df = pd.DataFrame(data)
df.to_csv('Crop_recommendation.csv', index=False)
print("✅ 'Crop_recommendation.csv' created successfully with dummy data!")