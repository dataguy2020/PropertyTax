def owneroccupancycondition(x):
    if x == "H":
        return "Yes"
    elif x == "N":
        return " No "
    else:
        return "0"


def yearcondition(x):
    if x == "O":
        return "1899"
    else:
        return x


def homesteadqualiticationcondition(x):
    if x == "A":
        return "Approved"
    if x == "X":
        return "Denied"
    else:
        return "No Application"

def test(owneroccupied, homesteadcode, exemptclass, year3countyrealestate, year3staterealestate, year3countycredit, year3statecredit):
    from rates import statetaxrate, annearundeltaxrate, annearundelsolidwaste, annearundelstormwater

#here for debugging/will be removed after verifying that this works. 
#   tanyardTH.loc[(tanyardTH['owneroccupancycode'] == 'Yes') & (tanyardTH['homesteadcreditqualificationcode'] == 'Approved'), 'year3total']\
#   = (tanyardTH['year3countyrealestate'] + tanyardTH['year3staterealestate'] - tanyardTH['year3countycredit'] - tanyardTH['year3statecredit'] +
#   annearundelsolidwaste + annearundelstormwater)

#   tanyardTH.loc[(tanyardTH['owneroccupancycode'] != 'Yes') | (tanyardTH['homesteadcreditqualificationcode'] != 'Approved'), 'year3total'] =
#   (tanyardTH['year3countyrealestate'] + tanyardTH['year3staterealestate'] + annearundelsolidwaste + annearundelstormwater)

    if (exemptclass != "Blank"):
        taxbill = annearundelsolidwaste + annearundelstormwater
        return taxbill
    if (exemptclass == "Blank"):
        if (owneroccupied == "Yes"):
            taxbill = year3countyrealestate + year3staterealestate - year3countycredit - year3statecredit + annearundelsolidwaste + annearundelstormwater
            return taxbill
        else:
            taxbill = year3countyrealestate + year3staterealestate + annearundelsolidwaste + annearundelstormwater
            return taxbill 
    else:
        taxbill = 0 
        return taxbill 
