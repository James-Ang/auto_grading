import pickle
import pandas as pd
from autograde_lib import get_data
from sklearn.tree import DecisionTreeClassifier

#%% IMPORTING DATA
marlipal_df = get_data('marlipal.json')

feature_cols = ['surf_concen_0.01g/l', 'cmc', 'EO_content', 'oh_value']
X = marlipal_df[feature_cols]
# y = marlipal_df.grade
y = marlipal_df.product_id.astype('str')

# Training
# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X,y)

with open('train_prodid.pickle', 'wb') as f:
    pickle.dump(clf, f)
