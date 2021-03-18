import pandas as pd
import numpy as np
from datetime import datetime

def load_data(cMonth, cYear, interval='1min'):

  if interval =='1min':
    path = '/gdrive/My Drive/Data/SoyBean_'+ cMonth + cYear+ '_1min.csv'

  if interval =='60min':
    path = '/gdrive/My Drive/Data/SoyBean_'+ cMonth + cYear+ '_60min.csv'

  if interval =='daily':
    path = '/gdrive/My Drive/Data/SoyBean_'+ cMonth + cYear+ '_1440min.csv'
  
  df = pd.read_csv(path)
  df.drop(labels='Unnamed: 0', axis=1,inplace=True)
  df['Date Time'] = pd.to_datetime(df['Timestamp'], infer_datetime_format= True)
  df.drop(labels='Timestamp', axis=1,inplace=True)
  df.set_index(keys='Date Time',inplace=True)
  df = df.rename(columns = {'Last':'Close'})
  daymask = (df.index <= df.index[-1]+pd.Timedelta(days=-16)) #& (df.index >= df.index[-1]+pd.Timedelta(days=-381))
  day_df = df.loc[daymask]
  night_data = day_df.between_time('00:00:00', '12:59:00')
  day_data = day_df.between_time('13:00:00', '19:00:00')

  return day_df, night_data, day_data

def resamplePeriod(df, period='5min'):
    logic = {'Open'  : 'first',
         'High'  : 'max',
         'Low'   : 'min',
         'Close' : 'last',
         'Volume': 'sum'}

    return df.resample(period).apply(logic).dropna()
