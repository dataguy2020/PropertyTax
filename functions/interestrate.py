def interestrate(county):
    if (county == "ANNE"):
        from interestRates import anneinterestrate
        countyinterestrate = anneinterestrate / 100
        return countyinterestrate
