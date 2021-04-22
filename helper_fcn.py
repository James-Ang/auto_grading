import pandas as pd

from lib import create_json

filename = r'autograding_v1.xlsx'

# MARLIPAL Data
marlipal_df = pd.read_excel(filename,sheet_name='marlipal')
# trucktype_df.drop(['truck_height_m','truck_width_m','truck_length_m'],axis=1, inplace=True)
marlipal.name = f'{marlipal_df=}'.split('=')[0]
create_json(marlipal_df)
