def taxcalculation(owneroccupied, homesteadcode, exemptclass, countyrealestate, staterealestate, countycredit, statecredit):
    from rates import annearundelsolidwaste, annearundelstormwater

    if (exemptclass != "Blank"):
        if (owneroccupied in ("Yes", "No")):
            taxbill = annearundelsolidwaste + annearundelstormwater
            return taxbill

    if (exemptclass == "Blank"):
        if (owneroccupied in ("Yes")):
            if (homesteadcode == "Approved"):
                taxbill = countyrealestate + staterealestate - countycredit - statecredit + annearundelsolidwaste + annearundelstormwater
                return taxbill
            elif (homesteadcode == "Denied"):
                taxbill = countyrealestate + staterealestate - countycredit - statecredit + annearundelsolidwaste + annearundelstormwater
                return taxbill
            elif (homesteadcode == "No Application"):
                taxbill = countyrealestate + staterealestate + annearundelsolidwaste + annearundelstormwater
                return taxbill
        else:
            taxbill = countyrealestate + staterealestate + annearundelsolidwaste + annearundelstormwater
            return taxbill 
    else:
        taxbill = 0 
        return taxbill 
