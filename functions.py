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
