import pandas as pd


def gat_passengers(age: int, fare: float) -> pd.DataFrame:
    '''Фильтрация пассажиров'''
    df = pd.read_csv('E:/Digital/bakend_programm/Project13/src/titanic.csv')
    price_and_age_df = df.loc[(df.Age < age) & (df.Fare < fare)]
    price_and_age_df.sort_values('Name', inplace=True)
    return price_and_age_df




if __name__ == '__main__':
    filtered_df = gat_passengers(age = 30, fare= 50.0)
    print(filtered_df.shape)
    print(filtered_df.head())