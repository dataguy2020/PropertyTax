# !/usr/bin/env python
author = "Michael Brown"

import pandas as pd
from limits import *
from rates import *

from warnings import simplefilter

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

tanyardTH = pd.read_csv('https://raw.githubusercontent.com/dataguy2020/PropertyTax/development/test/7651.csv')

#year 1 calcualtion
tanyardTH['year1difference'] = tanyardTH['box8'] - tanyardTH['box4']
tanyardTH['year1countylimit'] = tanyardTH['box4'] + (tanyardTH['box4'] * annearundelcountylimit)
tanyardTH['year1statelimit'] = tanyardTH['box4'] + (tanyardTH['box4'] * statelimit)
tanyardTH['year1countydifference'] = tanyardTH['box8'] - tanyardTH['year1countylimit']
tanyardTH['year1statedifference'] = tanyardTH['box8'] - tanyardTH['year1statelimit']

#year1 county credit calculation
tanyardTH.loc[tanyardTH['year1countydifference'] < 0, 'year1countycredit'] = 0
tanyardTH.loc[tanyardTH['year1countydifference'] > 0, 'year1countycredit'] = (tanyardTH['year1countydifference'] * annearundeltaxrate) / 100

#year 1 state credit calculation
tanyardTH.loc[tanyardTH['year1statedifference'] < 0, 'year1statecredit'] = 0
tanyardTH.loc[tanyardTH['year1statedifference'] > 0, 'year1statecredit'] = (tanyardTH[ 'year1statedifference'] * statetaxrate) / 100

#year 1 straight real estate tax payment without exempt class
tanyardTH['year1countyrealestate'] = (tanyardTH['box8'] * annearundeltaxrate) / 100
tanyardTH['year1staterealestate'] = (tanyardTH['box8'] * statetaxrate) / 100
tanyardTH['year1total'] = tanyardTH['year1countyrealestate'] + tanyardTH['year1staterealestate']  - tanyardTH['year1countycredit'] - tanyardTH['year1statecredit'] + annearundelsolidwaste + annearundelstormwater

#year 2 calculations
tanyardTH['year2difference'] = tanyardTH['box9'] - tanyardTH['year1countylimit']
tanyardTH['year2countylimit'] = tanyardTH['year1countylimit'] + (tanyardTH['year1countylimit'] * annearundelcountylimit)
tanyardTH['year2statelmit'] = tanyardTH['box2'] + (tanyardTH['box2'] * statelimit)
tanyardTH['year2countydifference'] = tanyardTH['box9'] - tanyardTH['year2countylimit']
tanyardTH['year2statedifference'] = tanyardTH['box9'] - tanyardTH['year2statelmit']

#year 2 county credit calculation
tanyardTH.loc[tanyardTH['year2countydifference'] < 0, 'year2countycredit'] = 0
tanyardTH.loc[tanyardTH['year2countydifference'] > 0, 'year2countycredit'] = (tanyardTH['year2countydifference'] * annearundeltaxrate) / 100

#yeaer 2 state credit calculation
tanyardTH.loc[tanyardTH['year2statedifference'] < 0, 'year2statecredit'] = 0
tanyardTH.loc[tanyardTH['year2statedifference'] > 0, 'year2statecredit'] = (tanyardTH[ 'year2statedifference'] * statetaxrate) / 100

#year 2 straight real estate tax payment without exempt class
tanyardTH['year2countyrealestate'] = (tanyardTH['box9'] * annearundeltaxrate) / 100
tanyardTH['year2staterealestate'] = (tanyardTH['box9'] * statetaxrate) / 100
tanyardTH['year2total'] = tanyardTH['year2countyrealestate'] + tanyardTH['year2staterealestate']  - tanyardTH['year2countycredit'] - tanyardTH['year2statecredit'] + annearundelsolidwaste + annearundelstormwater


# debugging
print(tanyardTH.dtypes)
print(tanyardTH)

tanyardTH.to_csv('7651.csv')
