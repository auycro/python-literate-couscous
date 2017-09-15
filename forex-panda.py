import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime
#import requests
import requests_cache
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


expire_after = datetime.timedelta(days=7)
session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)

#jpy = web.get_data_fred('DEXJPUS')
jpy = web.DataReader('DEXJPUS', 'fred', session=session)

indexes = jpy.index

#jpy.plot()
#plt.savefig('aui.png')

print('index',jpy.index)
print('columns',jpy.columns)
print('value',jpy.values)
print('describe',jpy.describe())

print('noww-------------')
aaa = pd.Series(jpy.DEXJPUS, index=pd.date_range('20170801', periods=30))

print(aaa)
