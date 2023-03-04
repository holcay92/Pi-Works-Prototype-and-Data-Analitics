import pandas as pd
import numpy as np

def impute_missing_vaccinations(filename):
    df = pd.read_csv(filename)

    min_daily_vaccinations = df.groupby('country')['daily_vaccinations'].min()
    df['daily_vaccinations'] = df['daily_vaccinations'].fillna(0)

    for country in df['country'].unique():
        relevant_countries = df[df['country'] != country]['country']
        relevant_min = min_daily_vaccinations[relevant_countries].min()
        idx = (df['country'] == country) & (df['daily_vaccinations'].isna())
        df.loc[idx, 'daily_vaccinations'] = relevant_min

    total_vaccinations = df[df['date'] == '2021-01-06']['daily_vaccinations'].sum()
    print("Total vaccinations on 1/6/2021: ", total_vaccinations)
    return df
