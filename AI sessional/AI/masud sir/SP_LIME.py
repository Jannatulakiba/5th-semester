import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from lime.lime_tabular import LimeTabularExplainer

# 1. Load dataset (example: Iris)
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
class_names = iris.target_names

# 2. Train/test split and optionally scale
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0, stratify=y
)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

# 3. Train classifier
clf = RandomForestClassifier(n_estimators=100, random_state=0)
clf.fit(X_train_s, y_train)

# 4. Create LIME explainer
explainer = LimeTabularExplainer(
    training_data = X_train_s,
    feature_names = feature_names,
    class_names   = class_names,
    discretize_continuous = True,
    random_state = 0
)

# 5. Generate LIME explanations for a subset of test instances
num_to_explain = len(X_test_s)  # or smaller subset
lime_explanations = []
for i in range(num_to_explain):
    x = np.array(X_test_s[i]).reshape(1, -1)
    exp = explainer.explain_instance(
        data_row=x.flatten(),
        predict_fn=clf.predict_proba,
        num_features=len(feature_names)
    )
    pred = int(clf.predict(x)[0])   # <-- convert here
    #list_feats = exp.as_list(label=pred)
   # lime_explanations.append((i, pred, list_feats))

# 6. Build a “feature coverage” scoring mechanism to pick representative instances
#    For simplicity, we define a set of important features across all explanations,
#    then pick the instances that cover most of them.

# Collect top features from all explanations
feature_set = set()
for (_, _, feat_list) in lime_explanations:
    for feat, weight in feat_list:
        feature_set.add(feat)  # or maybe feat name only

feature_list = list(feature_set)
print("Total unique features in explanations:", len(feature_list))

# Greedy pick: pick k instances that cover as many distinct features as possible
k = 5  # number of representative instances you want
selected = []
covered_features = set()
for _ in range(k):
    best_i = None
    best_gain = 0
    best_feats = None
    for (i, pred, feat_list) in lime_explanations:
        if i in selected:
            continue
        # features this instance would cover (that are not yet covered)
        feats = {feat for feat, w in feat_list}
        new_feats = feats - covered_features
        gain = len(new_feats)
        if gain > best_gain:
            best_gain = gain
            best_i = i
            best_feats = feats
    if best_i is None:
        break
    selected.append(best_i)
    covered_features |= best_feats
    print(f"Selected instance {best_i}, covering {len(best_feats)} new features")

print("Selected representative instances:", selected)
print("Covered features:", covered_features)

# 7. For the selected instances, present LIME explanations (text or plots)
for i in selected:
    x = X_test_s[i]
    exp = explainer.explain_instance(
        data_row = x,
        predict_fn = clf.predict_proba,
        num_features = len(feature_names)
    )
    pred = clf.predict(x.reshape(1,-1))[0]
    print("\n--- Explanation for test instance index", i,
          "predicted class:", class_names[pred])
    print(exp.as_list(label=pred))
    fig = exp.as_pyplot_figure(label=pred)
    fig.suptitle(f"SP-LIME explanation for instance {i}")
    plt.tight_layout()
    plt.show()
