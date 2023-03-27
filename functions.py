def owneroccupancycondition(x):
    if x == "H":
        return "Yes"
    elif x == "N":
        return "No"
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

def taxcalculation(owneroccupied, homesteadcode, exemptclass, countyrealestate, staterealestate, countycredit, statecredit):
    from rates import annearundelsolidwaste, annearundelstormwater

    if (exemptclass != "Blank"):
        if (owneroccupied == "Yes" | owneroccupied == "No"):
            taxbill = annearundelsolidwaste + annearundelstormwater
            return taxbill

    if (exemptclass == "Blank"):
        if (owneroccupied == "Yes"):
            if (homesteadcode == "Approved" or homesteadcode == "Denied"):
                taxbill = countyrealestate + staterealestate - countycredit - statecredit + annearundelsolidwaste + annearundelstormwater
                return taxbill
        else:
            taxbill = countyrealestate + staterealestate + annearundelsolidwaste + annearundelstormwater
            return taxbill 
    else:
        taxbill = 0 
        return taxbill 
