#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("opendata.maryland.gov", "6A6QgKxa0UQUr5fuWkqUSgFEa")

# Example authenticated client (needed for non-public datasets):
# client = Socrata(opendata.maryland.gov,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("n4fw-xcke", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

cleandata = results_df[['legal_description_line_2_mdp_field_legal2_sdat_field_18','record_key_account_number_sdat_field_3','assessment_cycle_year_sdat_field_399','current_assessment_year_total_phase_in_value_sdat_field_171','record_key_owner_occupancy_code_mdp_field_ooi_sdat_field_6','homestead_qualification_code_mdp_field_homqlcod_sdat_field_259','homestead_qualification_date_mdp_field_homqldat_sdat_field_260']].copy()
cleandata.to_csv('cleandata.csv')
cleandata

