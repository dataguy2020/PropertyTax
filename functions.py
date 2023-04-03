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
    
def countycredit(countydifference):
    from rates import annearundeltaxrate
    if (countydifference < 0):
        countycredit = 0
        return countycredit
    else:
        countycredit = (countydifference * annearundeltaxrate) / 100
        return countycredit
    
def statecredit(statedifference):
    from rates import statetaxrate 
    if (countycredit < 0):
        statecredit = 0
        return countycredit
    else:
        statecredit = (statedifference * statetaxrate) / 100
        return statecredit

def interestrate(county):
    if (county == "ANNE"):
        from interestRates import anneinterestrate
        countyinterestrate = anneinterestrate / 100
        return countyinterestrate


def semiannualpayments (owneroccupied, totalpayment, county):
    from interest import anneinterest 
    if (county == "ANNE"):
        if (owneroccupied == "Yes"):
            paymentone = totalpayment / 2
            paymenttwo = totalpayment - paymentone
            paymenttwo = (paymenttwo * (interestrate(county))) + paymenttwo
            return paymentone, paymenttwo
        else:
            paymentone = totalpayment
            paymenttwo = 0
            return paymentone, paymenttwo
    else:
        paymentone = 0
        paymenttwo = 0
        return paymentone, paymenttwo