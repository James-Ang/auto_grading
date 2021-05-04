import json
import pandas as pd
import pickle
from autograde_lib import select_grade

# Predict the response for test dataset
f = open('input.json',)
data_json = json.load(f)

# Copy from here
selected_grade = select_grade(data_json)

retJSON = {
    "selected_grade": selected_grade
            }
# To here
