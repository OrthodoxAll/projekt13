from statistics import mean

import pandas as pd

def pass_agg(df: pd.DataFrame) -> pd.DataFrame
    """Агрегация по классу """

    grouped_df = df.groupby('Pclass').agg(
        'Fare': 'mean',
        'PassengerId': 'count'
    })


if  __name__ == '__main__':
    df = pd.read_excel('winemag-data-130k.xlsx')