import numpy as np
import pandas as pd

df= pd.read_excel('winemag-data-130k-v2.xlsx')

new_df= df.groupby('country').agg({
    'price':'max',
    'points': 'sum'
})


print(new_df.head())
