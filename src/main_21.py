import pandas as pd


def get_servived(df: pd.DataFrame) -> int:
    """Записать файл выживших и вернуть их колличество"""
    servived_df = df[df['Survived'] == 1]
    servived_df.to_json('servived.json', orient='records',indent=4 , lines=True)
    return servived_df.count()



if __name__ == '__main__':
    df = pd.read_csv('E:/Digital/bakend_programm/Project13/src/titanic.csv')
    result = get_servived(df)
    print(result)
