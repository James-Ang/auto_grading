import os
import json
import pickle
import pandas as pd
import numpy as np
from datetime import datetime

# Saving to JSON file
def create_json(df):
    #df.to_json('test.json', orient='records')
    text = df.to_json(orient='records')
    json_object = json.loads(text)

    json_formatted_str = json.dumps(json_object, indent = 4)

    filename = df.name.split('_')[0]+'.json'

    with open(filename, 'w') as outfile:

        outfile.write(json_formatted_str)

def get_data(str):

    f = open(str, 'r')
    data = json.load(f)
    f.close()
    return pd.DataFrame(data)

def select_grade(data_json):
    predicted_grade = []

    dir_path = os.path.dirname(os.path.realpath(__file__))
    base_filename = 'train_prodid'
    filename_suffix = 'pickle'
    fullpath = os.path.join(dir_path, base_filename + "." + filename_suffix)
    print(dir_path)
    print(fullpath)

    specification_input = pd.DataFrame(data_json.get('specification_input'))

    with open(fullpath, 'rb') as f:
        clf = pickle.load(f)

    feature_cols = ['surf_concen_0.01g/l', 'cmc', 'EO_content', 'oh_value']

    X_test = specification_input[feature_cols]

    # X_test = [[35.5,17,69.2,83]]
    predicted_grade.append(clf.predict(X_test).item())

    return predicted_grade
