import pickle

with open('train.pickle', 'rb') as f:
    clf = pickle.load(f)

# Predict the response for test dataset
X_test = [[35.5,17,69.2,83]]
y_pred = clf.predict(X_test)
print(y_pred)
