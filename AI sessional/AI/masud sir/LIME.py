"""
LIME example for tabular data (Iris dataset).
- Trains a RandomForestClassifier.
- Uses lime.lime_tabular.TabularExplainer to explain a single prediction.
- Shows textual and matplotlib bar plot explanation.
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from lime.lime_tabular import LimeTabularExplainer
import matplotlib.pyplot as plt

# 1. Load data
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
class_names = iris.target_names

# 2. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Optional: scale features (LIME works with raw or scaled; be consistent)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Train a classifier
clf = RandomForestClassifier(n_estimators=200, random_state=42)
clf.fit(X_train_scaled, y_train)

# 4. Pick an instance to explain
instance_idx = 3  # pick an index from X_test
x_instance = X_test_scaled[instance_idx].reshape(1, -1)

# 5. Create a LIME TabularExplainer
explainer = LimeTabularExplainer(
    X_train_scaled,
    feature_names=feature_names,
    class_names=class_names,
    discretize_continuous=True,
    random_state=42
)

# 6. Explain the instance (explain_class is the class index to explain)
exp = explainer.explain_instance(
    data_row=x_instance.flatten(),
    predict_fn=clf.predict_proba,
    num_features=4,         # top features to show
    top_labels=3            # number of labels to generate explanation for
)

# 7. Print explanation for the predicted class
pred_proba = clf.predict_proba(x_instance)[0]
pred_class = np.argmax(pred_proba)
print(f"Predicted class: {class_names[pred_class]} (proba={pred_proba[pred_class]:.3f})")
print("LIME explanation (feature contributions) for the predicted class:\n")
for feature, weight in exp.as_list(label=pred_class):
    print(f"  {feature} -> {weight:.4f}")

# 8. Show a matplotlib plot (bar chart) of the explanation
fig = exp.as_pyplot_figure(label=pred_class)
fig.suptitle(f"LIME explanation for instance {instance_idx} -> {class_names[pred_class]}")
plt.tight_layout()
plt.show()

# 9. Optional: show explanation for all top labels
print("\nDetailed explanation for top labels:")
for label in exp.top_labels:
    print(f"\nLabel {label} ({class_names[label]}):")
    for feat, w in exp.as_list(label=label):
        print(f"  {feat} -> {w:.4f}")
