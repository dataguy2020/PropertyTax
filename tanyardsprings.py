#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import datetime as dt

from auth import applicationtoken
from babel.numbers import format_currency
#importing personal modules
from functions import *
import pandas as pd
import seaborn as sns
from sodapy import Socrata

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
cleandata.rename(columns={'legal_description_line_2_mdp_field_legal2_sdat_field_18': 'address'}, inplace=True)

#copying over columns from originating data frame
cleandata['accountnumber'] = results_df['record_key_account_number_sdat_field_3']
cleandata['opendataupdate'] = results_df['date_of_most_recent_open_data_portal_record_update']
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

cleandata['box2'] = results_df['current_assessment_year_total_assessment_sdat_field_172']
cleandata['box4'] = results_df['prior_assessment_year_total_assessment_sdat_field_161']
cleandata['box5'] = results_df['current_cycle_data_land_value_mdp_field_names_nfmlndvl_curlndvl_and_sallndvl_sdat_field_164']
cleandata['box6'] = results_df['current_cycle_data_improvements_value_mdp_field_names_nfmimpvl_curimpvl_and_salimpvl_sdat_field_165']
cleandata['box8'] = cleandata['box2']

#Conerting all to numeric
cleandata['box2'] = pd.to_numeric(cleandata['box2'])
cleandata['box4'] = pd.to_numeric(cleandata['box4'])
cleandata['box5'] = pd.to_numeric(cleandata['box5'])
cleandata['box6'] = pd.to_numeric(cleandata['box6'])
cleandata['box8'] = pd.to_numeric(cleandata['box8'])

cleandata['box7'] = (cleandata['box5'] + cleandata['box6'])
cleandata['box9a'] = ((cleandata['box7'] - cleandata['box4'])/3)
cleandata['box9'] = (cleandata['box9a'] + cleandata['box8'])

cleandata['box10'] = cleandata['box7']
cleandata['box7'] = pd.to_numeric(cleandata['box7'])
cleandata['box9'] = pd.to_numeric(cleandata['box9'])
cleandata['box10'] = pd.to_numeric(cleandata['box10'])



#DEBUGGING
#print columns & types
#print(cleandata.dtypes)

cleandata['totalchange'] = cleandata['box7'] - cleandata['box4']

#converting
cleandata['assessmentyear'] = [dt.datetime.strptime(x, '%Y').year for x in cleandata['assessmentyear']]
cleandata['accountnumber'] = pd.to_numeric(cleandata['accountnumber'])
cleandata['key'] = pd.to_numeric(cleandata['key'])

#setting index
cleandata = cleandata.set_index('key')

#converting conditions
cleandata['owneroccupancycode'] = cleandata['owneroccupancycode'].apply(owneroccupancycondition)
cleandata['homesteadcreditqualificationcode'] = cleandata['homesteadcreditqualificationcode'].apply(
    homesteadqualiticationcondition)

#Removing bad data points
#These are common areas or open areas that are not owned by a resident but by the Association
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
#There is one townhome that is listed as SF and the rest are blank
cleandata.loc[cleandata["accountnumber"] == 60590243390, "housetype"] = "TH"
cleandata.loc[cleandata["accountnumber"] == 60590254221, "housetype"] = "TH"
cleandata.loc[cleandata["accountnumber"] == 60590254222, "housetype"] = "TH"
cleandata.loc[cleandata["accountnumber"] == 60590254223, "housetype"] = "TH"
cleandata.loc[cleandata["accountnumber"] == 60590254224, "housetype"] = "TH"

#Updating year built 
cleandata.loc[cleandata["accountnumber"] == 79790230860, "yearbuilt"] = "2011"
cleandata.loc[cleandata["accountnumber"] == 79790230900, "yearbuilt"] = "2010"
cleandata.loc[cleandata["accountnumber"] == 79790234258, "yearbuilt"] = "2013"

cleandata['yearbuilt'] = cleandata['yearbuilt'].apply(yearcondition)

#Debugging to see number of unique housetypes and how many 
print(cleandata['housetype'].value_counts())

#Debugging to see owner occupancy status of all homes
print(cleandata['owneroccupancycode'].value_counts())

#Debugging to see when homes were built
print(cleandata['yearbuilt'].value_counts().sort_index(0))


#Saving to CSV
cleandata.to_csv('cleandata.csv')

#printing data frame to screen
cleandata

cleandata["totalchange"] = pd.to_numeric(cleandata["totalchange"])
averagechange = cleandata["totalchange"].mean()
#print (averagechange)
averagechange = "${:,.2f}".format(averagechange)
print('The average home assessment change in Tanyard Springs is ', averagechange) 

