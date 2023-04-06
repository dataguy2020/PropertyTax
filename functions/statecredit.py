def statecredit(statedifference):
    from rates import statetaxrate 
    if (countycredit < 0):
        statecredit = 0
        return countycredit
    else:
        statecredit = (statedifference * statetaxrate) / 100
        return statecredit
