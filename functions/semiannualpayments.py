def semiannualpayments (row):
    owneroccupied, totalpayment, county = row  # Unpack the values from the row
    if (county == "ANNE"):
        from interest import anneinterest  # Put all imports at the top of the module.  anneinterest not used
        if (owneroccupied == "Yes"):
            paymentone = totalpayment / 2
            paymenttwo = totalpayment - paymentone
            paymenttwo = (paymenttwo * (interestrate(county))) + paymenttwo
        else:
            paymentone = totalpayment
            paymenttwo = 0
    else:
        paymentone = 0
        paymenttwo = 0
    return paymentone, paymenttwo