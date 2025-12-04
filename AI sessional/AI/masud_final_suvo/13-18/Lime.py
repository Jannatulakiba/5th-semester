from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import lime
import lime.lime_tabular

# Load dataset
data = load_iris()
X, y = data.data, data.target

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Create LIME explainer
explainer = lime.lime_tabular.LimeTabularExplainer(
    training_data=X,
    feature_names=data.feature_names,
    class_names=data.target_names,
    mode='classification'
)

# Explain one instance (you can change X[0] to any index)
instance_index = 0
exp = explainer.explain_instance(X[instance_index], model.predict_proba)

# ---- Print results in console ----
print("\n LIME Explanation for Instance:", instance_index)
print("Predicted class:", data.target_names[model.predict([X[instance_index]])[0]])
print("True class:", data.target_names[y[instance_index]])
print("\nFeature contributions (weight shows importance):\n")

# exp.as_list() gives feature -> weight pairs
for feature, weight in exp.as_list():
    print(f"{feature:40s} => weight: {weight:.4f}")

print("\nExplanation complete ")
