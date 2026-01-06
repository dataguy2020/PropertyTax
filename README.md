# PropertyTax
This script is set up to pull public avaiable data for the community of Tanyard Springs (currently) and to calculate the house assessment, the 2% and 10% caps allowed by Anne Arundel County & the State of Maryland, along with the property tax payment (yearly) and semi-annual payment that is needed for each of the homes. Our goal is to make this available to be run for any county. At no time does this information pull any names of current owners from any other database. We pull strictly from government-run public API via opendata.maryland.gov. We have no intention to utilize other non government-run APIs at this time. 

You have will have to obtain your own personal authentication token from https://opendata.maryland.gov. There is an example file called, auth.py.example. This file will need to be updated and then renamed to auth.py. 

# DISCLAIMER
This project is not affiliated with the State of Maryland or any of its 24 jurisdictions. This project is pulling data that is avaiable via a public database that is accessible to all persons

# TO DO UPADATS
* Update to work with the FY26 data
* Update to work with the FY27 data

# TO DO CLEAN-UP
* Clean- up functions

# TO DO EXPANSION PLAN 1
* Calculate property taxes that are due in a annual payment setup
* Calculate property taxes that are due in a semi annual payment setup

# TO DO EXPANSION PLAN 2
* Expand the script to include the rest of Anne Arundel County
* Expand the script to include Counties that border AA (Baltimore City, Baltimore County, Howard County, Calvert County, Prince George's, Queen Anne's)
* Expand the script to include the rest of the Eastern Shore (Caroline, Cecil, Dorchester, Kent, Somerset, Tablot, Wicomico, Worcester)
* Expand the script to include the rest of Central Maryland (Carroll, Harford)
* Expand the script to include western Maryland Counties (Washington, Allegany, Garrett)
* Expand the script to include the DC Metro Countries (Fredrick, Montgomery)
* Expand the script to include the Southern Maryland Counties (Calvert, Charles, St. Marys)

# Notes
* Under the two-payment plan, the local governments may add a service fee of up to 1.65% of the second payment to your tax bill. This amount is to compensate the local government for lost interest and additional administrative expenses of sending two tax bills. This fee will be added to the second payment.
