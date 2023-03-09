# !/usr/bin/env python
author = "Michael Brown"

import pandas as pd
from limits import *

from warnings import simplefilter

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

tanyardTH = pd.read_csv('https://raw.githubusercontent.com/dataguy2020/PropertyTax/development/test/7651.csv')

tanyardTH['year1difference'] = tanyardTH['box8'] - tanyardTH['box4']
tanyardTH['year1countylimit'] = tanyardTH['box4'] + (tanyardTH['box4'] * annearundelcountylimit)
tanyardTH['year1statelimit'] = tanyardTH['box4'] + (tanyardTH['box4'] * statelimit)

# debugging
print(tanyardTH.dtypes)
print(tanyardTH)
