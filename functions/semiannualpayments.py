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
