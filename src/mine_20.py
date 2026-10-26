from statistics import mean

import pandas as pd

from src.main import result


def pass_agg(df: pd.DataFrame):
    """Агрегация по классу """

    grouped_df = df.groupby('Pclass').agg({
        'Fare': 'mean',
        'PassengerId': 'count'
    })
    dict_data = grouped_df.to_dict(orient='records')

    result = dict()

    for index, item in enumerate(dict_data):
        result[ f'{index+1}'] ={
            'average_ticket_price' : item['Fare'],
          'passenger_count' : item['PassengerId']
          }

    return result


if  __name__ == '__main__':
    df = pd.read_csv('E:/Digital/bakend_programm/Project13/src/titanic.csv')
    result = pass_agg(df)
    print(result)