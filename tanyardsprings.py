#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata
import datetime as dt
from babel.numbers import format_currency

#importing personal modules
from functions import  *
from auth import applicationtoken

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("opendata.maryland.gov", applicationtoken)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(opendata.maryland.gov,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("q4mw-f34p", limit=3000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
results_df.to_csv('results_df.csv')


#creating dataframe + adding first field from the originating data frame
cleandata = results_df[['legal_description_line_2_mdp_field_legal2_sdat_field_18']].copy()

#changing column name in data frame
cleandata.rename(columns = {'legal_description_line_2_mdp_field_legal2_sdat_field_18':'address'}, inplace = True)

#copying over columns from originating data frame
cleandata['accountnumber'] = results_df['record_key_account_number_sdat_field_3']
cleandata['key'] = cleandata['accountnumber']
cleandata['housetype'] = results_df['mdp_street_address_type_code_mdp_field_resityp']
cleandata['landuse'] = results_df['land_use_code_mdp_field_lu_desclu_sdat_field_50']
cleandata['exemptclass'] = results_df['exempt_class_mdp_field_exclass_descexcl_sdat_field_49']
cleandata['assessmentyear'] = results_df['assessment_cycle_year_sdat_field_399']
cleandata['currentyeartotalassessment'] = results_df['current_assessment_year_total_phase_in_value_sdat_field_171']
cleandata['owneroccupancycode'] = results_df['record_key_owner_occupancy_code_mdp_field_ooi_sdat_field_6']
cleandata['homesteadcreditqualificationcode'] = results_df['homestead_qualification_code_mdp_field_homqlcod_sdat_field_259']
cleandata['homesteadqualificationdate'] = results_df['homestead_qualification_date_mdp_field_homqldat_sdat_field_260']
cleandata['yearbuilt'] = results_df['c_a_m_a_system_data_year_built_yyyy_mdp_field_yearblt_sdat_field_235']
cleandata['datepurchased'] = results_df['sales_segment_1_transfer_date_yyyy_mm_dd_mdp_field_tradate_sdat_field_89']
cleandata['zoning'] = results_df['zoning_code_mdp_field_zoning_sdat_field_45']

#converting
cleandata['assessmentyear'] = [dt.datetime.strptime(x, '%Y').year for x in cleandata['assessmentyear']]
cleandata['accountnumber'] = pd.to_numeric(cleandata['accountnumber'])
cleandata['key'] = pd.to_numeric(cleandata['key'])

#setting index
cleandata = cleandata.set_index('key')

#formatting the data a bit further   
cleandata['owneroccupancycode'] = cleandata['owneroccupancycode'].apply(owneroccupancycondition)
cleandata['yearbuilt'] = cleandata['yearbuilt'].apply(yearcondition)
cleandata['homesteadcreditqualificationcode'] = cleandata['homesteadcreditqualificationcode'].apply(homesteadqualiticationcondition)
cleandata["currentyeartotalassessment"] = cleandata["currentyeartotalassessment"].apply(lambda x: format_currency(x, currency="USD", locale="en_US"))

#print columns & types
print(cleandata.dtypes)

#Removing bad data points
cleandata = cleandata.drop(60590243392)
cleandata = cleandata.drop(60590243393)
cleandata = cleandata.drop(60590243394)
cleandata = cleandata.drop(79790223423)
cleandata = cleandata.drop(79790223432)
cleandata = cleandata.drop(79790223433)
cleandata = cleandata.drop(79790231070)
cleandata = cleandata.drop(79790231447)
cleandata = cleandata.drop(79790234449)
cleandata = cleandata.drop(79790235116)
cleandata = cleandata.drop(79790240734)
cleandata = cleandata.drop(79790240735)
cleandata = cleandata.drop(79790240744)
cleandata = cleandata.drop(79790245914)

#Modifying field value to be "TH"
cleandata.loc[cleandata["accountnumber"] == 60590243390, "housetype"] = "TH"
cleandata.loc[cleandata["accountnumber"] == 60590254221, "housetype"] = "TH"
cleandata.loc[cleandata["accountnumber"] == 60590254222, "housetype"] = "TH"
cleandata.loc[cleandata["accountnumber"] == 60590254223, "housetype"] = "TH"
cleandata.loc[cleandata["accountnumber"] == 60590254224, "housetype"] = "TH"

#Debugging to see number of unique housetypes and how many 
print(cleandata['housetype'].value_counts())

#Saving to CSV
cleandata.to_csv('cleandata.csv')

#printing data frame to screen
cleandata

