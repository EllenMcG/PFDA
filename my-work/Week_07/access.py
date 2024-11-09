# separate python file of access.log file analysis from the lab_07_02.ipynb

# import modules 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import re 
from datetime import datetime
import pytz

def parse_str(x):
    """
    Returns the string delimited by two characters such as [].

    Parameters 
        x (str): input string that is delimited 
    """
    return x[1:-1]


def parse_datetime(x):
    '''
    Parses datetime with timezone formatted as:
        `[day/month/year:hour:minute:second zone]`

    Example:
        `>>> parse_datetime('13/Nov/2015:11:45:42 +0000')`
        `datetime.datetime(2015, 11, 3, 11, 45, 4, tzinfo=<UTC>)`
        
    '''
    dt = datetime.strptime(x[1:-1], '%d/%b/%Y:%H:%M:%S')
    return dt


df = pd.read_csv(
    'access.log',
    sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
    engine='python',
    na_values='-',
    header=None,
    usecols=[0, 3, 4, 5, 6, 7, 8],
    names=['ip', 'time', 'request', 'status', 'size', 'referer', 'user_agent'],
    converters={'time': parse_datetime,
                'request': parse_str,
                'status': int,
                'size': int,
                'referer': parse_str,
                'user_agent': parse_str})

request = df.pop('request').str.split()
df['resource'] = request.str[1]
df['method'] = request.str[0]
df['url'] = request.str[1].str.split('?').str[0] 

# resampling ecvery hour and getting a sum
dfbyhour =df.resample('h',on='time').sum()

dfbyhour['hour'] = dfbyhour.index.hour
dfbyhour['date'] = dfbyhour.index.date

# resisual plot with 1st order polynomial 
sns.residplot(x="hour", y="size", data=dfbyhour, order=1)
plt.show()