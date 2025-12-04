from lime.lime_tabular import LimeTabularExplainer
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# --- 1. Load dataset ---
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
class_names = iris.target_names

# --- 2. Train-test split ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 3. Train a simple model ---
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
print("Model trained successfully!")

# --- 4. Initialize LIME explainer ---
explainer = LimeTabularExplainer(
    X_train,
    feature_names=feature_names,
    class_names=class_names,
    discretize_continuous=True
)

# --- 5. Pick one test sample to explain ---
i = 0
sample = X_test[i]
pred_class = model.predict([sample])[0]

print("\nActual class:", class_names[y_test[i]])
print("Predicted class:", class_names[pred_class])

# --- 6. Explain prediction ---
exp = explainer.explain_instance(sample, model.predict_proba, num_features=4)

# Show top features in terminal
print("\nTop features affecting prediction:")
for feature, weight in exp.as_list():
    print(f"{feature}: {weight:.3f}")

# Optional: Save HTML visualization
exp.save_to_file("lime_explanation.html")
print("\nLIME explanation saved to lime_explanation.html")
