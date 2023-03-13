# !/usr/bin/env python
author = "Michael Brown"

import pandas as pd
from limits import *
from rates import *

from warnings import simplefilter

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

tanyardTH = pd.read_csv('https://raw.githubusercontent.com/dataguy2020/PropertyTax/development/test/7651.csv')

tanyardTH['year1difference'] = tanyardTH['box8'] - tanyardTH['box4']
tanyardTH['year1countylimit'] = tanyardTH['box4'] + (tanyardTH['box4'] * annearundelcountylimit)
tanyardTH['year1statelimit'] = tanyardTH['box4'] + (tanyardTH['box4'] * statelimit)
tanyardTH['year1countydifference'] = tanyardTH['box8'] - tanyardTH['year1countylimit']
tanyardTH['year1statedifference'] = tanyardTH['box8'] - tanyardTH['year1statelimit']
tanyardTH.loc[tanyardTH['year1countydifference'] < 0, 'year1countycredit'] = 0
tanyardTH.loc[tanyardTH['year1countydifference'] > 0, 'year1countycredit'] = (tanyardTH['year1countydifference'] * annearundeltaxrate) / 100
tanyardTH.loc[tanyardTH['year1statedifference'] < 0, 'year1statecredit'] = 0
tanyardTH.loc[tanyardTH['year1statedifference'] > 0, 'year1statecredit'] = (tanyardTH[ 'year1statedifference'] * statetaxrate) / 100
tanyardTH['year1countyrealestate'] = (tanyardTH['box8'] * annearundeltaxrate) / 100
tanyardTH['year1staterealestate'] = (tanyardTH['box8'] * statetaxrate) / 100
tanyardTH['year1total'] = tanyardTH['year1countyrealestate'] + tanyardTH['year1staterealestate']  - tanyardTH['year1countycredit'] - tanyardTH['year1statecredit'] + annearundelsolidwaste + annearundelstormwater

tanyardTH['year2difference'] = tanyardTH['box9'] - tanyardTH['year1countylimit']
tanyardTH['year2countylimit'] = tanyardTH['year1countylimit'] + (tanyardTH['year1countylimit'] * annearundelcountylimit)

# debugging
print(tanyardTH.dtypes)
print(tanyardTH)

tanyardTH.to_csv('output/7651.csv')
