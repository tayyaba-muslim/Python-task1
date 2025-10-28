import pandas as pd
import numpy as np

data = {
    'Name': ['Ali', 'Sara', 'Bilal', 'Ayesha', 'Omar'],
    'English': [80, 70, np.nan, 50, 90],
    'Maths': [85, np.nan, 60, 40, 95],
    'Urdu': [75, 65, 55, np.nan, 80]
}

df = pd.DataFrame(data)

df.fillna(40, inplace=True)

df['Percentage'] = df[['English', 'Maths', 'Urdu']].mean(axis=1)

df['Result'] = df['Percentage'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')

print(df)
