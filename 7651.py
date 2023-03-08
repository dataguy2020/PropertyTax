# !/usr/bin/env python
author = "Michael Brown"

import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
from datetime import timedelta
import seaborn as sns


#from warnings import simplefilter
#simplefilter(action="ignore", category=pd.errors.PerformanceWarning)


tanyardTH = pd.read_csv('https://raw.githubusercontent.com/dataguy2020/PropertyTax/development/test/7651.csv')

print(tanyardTH.dtypes)
