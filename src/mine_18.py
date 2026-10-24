from encodings import utf_8

import pandas as pd
import json

df = pd.read_csv('E:/Digital/bakend_programm/Project13/src/titanic.csv', encoding='utf-8')

def filter_passengers(df):
    result_df = df[((df['Sex'] == 'male') & (df['Age'] > 50)) | ((df['Sex'] == 'female') & (df['Age'] < 30))]
    return result_df.to_json(orient='records')

print(filter_passengers(df))
