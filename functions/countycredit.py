def countycredit(countydifference):
    from rates import annearundeltaxrate
    if (countydifference < 0):
        countycredit = 0
        return countycredit
    else:
        countycredit = (countydifference * annearundeltaxrate) / 100
        return countycredit
