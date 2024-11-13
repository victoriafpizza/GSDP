def simulate_tariff_growth(year, initial_tariff, increment_rate, memo={}):
    if year in memo:
        return memo[year]
    
    if year == 0:
        tariff = initial_tariff
    else:
        previous_tariff = simulate_tariff_growth(year - 1, initial_tariff, increment_rate, memo)
        tariff = previous_tariff * (1 + increment_rate)

    memo[year] = tariff
    return tariff
