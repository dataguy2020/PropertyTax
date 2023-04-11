def semiannualpayments1 (owneroccupied, totalpayment, county):
    if (county == "ANNE"):
        from interest import anneinterest
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