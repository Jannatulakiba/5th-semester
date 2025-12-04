from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load data
data = load_iris()
X, y = data.data, data.target

# Train model
model = DecisionTreeClassifier(criterion='entropy', random_state=42)
model.fit(X, y)

# Visualize
plt.figure(figsize=(10, 6))
plot_tree(model, filled=True, feature_names=data.feature_names, class_names=data.target_names)
plt.show()
