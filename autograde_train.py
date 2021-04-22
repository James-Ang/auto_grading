import pickle
import pandas as pd
from lib import get_data
from sklearn.tree import DecisionTreeClassifier

#%% IMPORTING DATA
marlipal_df = get_data('marlipal.json')

feature_cols = ['surf_concen_0.01g/l', 'cmc', 'EO_content', 'oh_value']
X = marlipal_df[feature_cols]
y = marlipal_df.grade

# Training
# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X,y)

with open('train.pickle', 'wb') as f:
    pickle.dump(clf, f)


with open('train.pickle', 'rb') as f:
    clf = pickle.load(f)


# Predict the response for test dataset
X_test = [[35.5,17,69.2,83]]
y_pred = clf.predict(X_test)
print(y_pred)
