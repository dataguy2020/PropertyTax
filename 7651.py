# !/usr/bin/env python
author = "Michael Brown"

import pandas as pd
from limits import statelimit, annearundelcountylimit
from rates import statetaxrate, annearundeltaxrate, annearundelsolidwaste, annearundelstormwater
from warnings import simplefilter
from functions import taxcalculation, semiannualpayments, semiannualpayments1

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

tanyardTH = pd.read_csv('test/7651b.csv')

year1=tanyardTH['assessmentyear']
year2=year1+1
year3=year2+1

# year 1 calculation
tanyardTH['year1difference'] = tanyardTH['box8'] - tanyardTH['box4']
tanyardTH['year1countylimit'] = tanyardTH['box4'] + (tanyardTH['box4'] * annearundelcountylimit)
tanyardTH['year1statelimit'] = tanyardTH['box4'] + (tanyardTH['box4'] * statelimit)
tanyardTH['year1countydifference'] = tanyardTH['box8'] - tanyardTH['year1countylimit']
tanyardTH['year1statedifference'] = tanyardTH['box8'] - tanyardTH['year1statelimit']

# year1 county credit calculation
tanyardTH.loc[tanyardTH['year1countydifference'] < 0, 'year1countycredit'] = 0
tanyardTH.loc[tanyardTH['year1countydifference'] > 0, 'year1countycredit'] = (tanyardTH[
                                                                                  'year1countydifference'] * annearundeltaxrate) / 100

# year 1 state credit calculation
tanyardTH.loc[tanyardTH['year1statedifference'] < 0, 'year1statecredit'] = 0
tanyardTH.loc[tanyardTH['year1statedifference'] > 0, 'year1statecredit'] = (tanyardTH[
                                                                                'year1statedifference'] * statetaxrate) / 100

# year 1 straight real estate tax payment without exempt class
tanyardTH['year1countyrealestate'] = (tanyardTH['box8'] * annearundeltaxrate) / 100
tanyardTH['year1staterealestate'] = (tanyardTH['box8'] * statetaxrate) / 100
tanyardTH["year1total"] = tanyardTH.apply(
    lambda x: taxcalculation(x["owneroccupancycode"], x["homesteadcreditqualificationcode"], x["exemptclass"],
                             x["year1countyrealestate"], x["year1staterealestate"], x["year1countycredit"],
                             x["year1statecredit"]), axis=1)

# year 2 calculation
tanyardTH['year2countylimit'] = tanyardTH['year1countylimit'] + (tanyardTH['year1countylimit'] * annearundelcountylimit)
tanyardTH['year2statelmit'] = tanyardTH['box2'] + (tanyardTH['box2'] * statelimit)
tanyardTH['year2countydifference'] = tanyardTH['box9'] - tanyardTH['year2countylimit']
tanyardTH['year2statedifference'] = tanyardTH['box8'] - tanyardTH['year2statelmit']

# year 2 county credit calculation
tanyardTH.loc[tanyardTH['year2countydifference'] < 0, 'year2countycredit'] = 0
tanyardTH.loc[tanyardTH['year2countydifference'] > 0, 'year2countycredit'] = (tanyardTH[
                                                                                  'year2countydifference'] * annearundeltaxrate) / 100

# year 2 state credit calculation
tanyardTH.loc[tanyardTH['year2statedifference'] < 0, 'year2statecredit'] = 0
tanyardTH.loc[tanyardTH['year2statedifference'] > 0, 'year2statecredit'] = (tanyardTH[
                                                                                'year2statedifference'] * statetaxrate) / 100

# year 2 straight real estate tax payment without exempt class
tanyardTH['year2countyrealestate'] = (tanyardTH['box9'] * annearundeltaxrate) / 100
tanyardTH['year2staterealestate'] = (tanyardTH['box9'] * statetaxrate) / 100
tanyardTH["year2total"] = tanyardTH.apply(
    lambda x: taxcalculation(x["owneroccupancycode"], x["homesteadcreditqualificationcode"], x["exemptclass"],
                             x["year2countyrealestate"], x["year2staterealestate"], x["year2countycredit"],
                             x["year2statecredit"]), axis=1)

# year 3 calculation
tanyardTH['year3countylimit'] = tanyardTH['year2countylimit'] + (tanyardTH['year2countylimit'] * annearundelcountylimit)
tanyardTH['year3statelimit'] = tanyardTH['box9'] + (tanyardTH['box9'] * statelimit)
tanyardTH['year3countydifference'] = tanyardTH['box10'] - tanyardTH['year3countylimit']
tanyardTH['year3statedifference'] = tanyardTH['box9'] - tanyardTH['year3statelimit']

# year 3 county credit calculation
tanyardTH.loc[tanyardTH['year3countydifference'] < 0, 'year3countycredit'] = 0
tanyardTH.loc[tanyardTH['year3countydifference'] > 0, 'year3countycredit'] = (tanyardTH[
                                                                                  'year3countydifference'] * annearundeltaxrate) / 100

# year 3 state credit calculation
tanyardTH.loc[tanyardTH['year3statedifference'] < 0, 'year3statecredit'] = 0
tanyardTH.loc[tanyardTH['year3statedifference'] > 0, 'year3statecredit'] = (tanyardTH[
                                                                                'year3statedifference'] * statetaxrate) / 100

# year3 straight real estate tax payment without exempt class
tanyardTH['year3countyrealestate'] = (tanyardTH['box10'] * annearundeltaxrate) / 100
tanyardTH['year3staterealestate'] = (tanyardTH['box10'] * statetaxrate) / 100

tanyardTH["year3total"] = tanyardTH.apply(
    lambda x: taxcalculation(x["owneroccupancycode"], x["homesteadcreditqualificationcode"], x["exemptclass"],
                             x["year3countyrealestate"], x["year3staterealestate"], x["year3countycredit"],
                             x["year3statecredit"]), axis=1)
tanyardTH["year3paytest"] = tanyardTH.apply(lambda x: semiannualpayments1(x["owneroccupancycode"], x["year3total"], x["county"]),
                                            axis=1)
tanyardTH["year3pay1"] = tanyardTH["year3paytest"][0][0]
tanyardTH["year3pay2"] = tanyardTH["year3paytest"][0][1]

# debugging
# print(tanyardTH.dtypes)
print(tanyardTH)
tanyardTH.to_csv('output/7651.csv')
