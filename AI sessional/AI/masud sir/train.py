import math

# Sample dataset (Outlook, Temperature, PlayTennis)
dataset = [
    ['Sunny', 'Hot', 'No'],
    ['Sunny', 'Hot', 'No'],
    ['Overcast', 'Hot', 'Yes'],
    ['Rain', 'Mild', 'Yes'],
    ['Rain', 'Cool', 'Yes'],
    ['Rain', 'Cool', 'No'],
    ['Overcast', 'Cool', 'Yes'],
    ['Sunny', 'Mild', 'No'],
    ['Sunny', 'Cool', 'Yes'],
    ['Rain', 'Mild', 'Yes'],
    ['Sunny', 'Mild', 'Yes'],
    ['Overcast', 'Mild', 'Yes'],
    ['Overcast', 'Hot', 'Yes'],
    ['Rain', 'Mild', 'No']
]

# Train function
def train_naive_bayes(data):
    label_counts = {}
    feature_counts = {}

    for row in data:
        outlook, temp, label = row
        label_counts[label] = label_counts.get(label, 0) + 1
        if label not in feature_counts:
            feature_counts[label] = {"Outlook": {}, "Temp": {}}

        feature_counts[label]["Outlook"][outlook] = feature_counts[label]["Outlook"].get(outlook, 0) + 1
        feature_counts[label]["Temp"][temp] = feature_counts[label]["Temp"].get(temp, 0) + 1

    return label_counts, feature_counts


#P(Yes | Sunny, Cool) ≈ 59.8%

#P(No | Sunny, Cool) ≈ 40.2% 

# Predict with posterior probabilities
def predict_with_posteriors(x, label_counts, feature_counts):
    total = sum(label_counts.values())
    probs = {}

    for label in label_counts:
        probs[label] = label_counts[label] / total  # Prior
        for i, feature in enumerate(["Outlook", "Temp"]):
            value = x[i]
            count = feature_counts[label][feature].get(value, 0)
            probs[label] *= (count + 1) / (label_counts[label] + len(feature_counts[label][feature]))

    # Normalize to get posterior probabilities
    total_prob = sum(probs.values())
    posteriors = {label: probs[label] / total_prob for label in probs}

    # Pick best class
    prediction = max(posteriors, key=posteriors.get)
    return prediction, posteriors


# Train
label_counts, feature_counts = train_naive_bayes(dataset)

# Test
test_sample = ['Sunny', 'Cool']
prediction, posteriors = predict_with_posteriors(test_sample, label_counts, feature_counts)

print("Test Sample:", test_sample)
print("Predicted Class:", prediction)
print("Posterior Probabilities:", posteriors)
