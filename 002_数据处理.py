import pandas as pd
import numpy as np
import dask.dataframe as dd


if __name__ == '__main__':
    # weather_csv = pd.read_csv('./weather.csv')
    weather_csv = dd.read_csv('./weather.csv', dtype={'a': str, 'c': str})

    weather_csv = weather_csv.drop(labels='j', axis=1)
    weather_csv = weather_csv.drop_duplicates()

    weather_csv.to_csv('./weather_new_3.csv', mode='w', index=None)
    print('结束....')
