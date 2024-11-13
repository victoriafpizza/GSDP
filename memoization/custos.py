def calculate_total_cost(year, initial_cost, annual_maintenance_cost, efficiency_loss_rate, memo={}):
    if year in memo:
        return memo[year]
    
    if year == 0:
        cost = initial_cost
    else:
        previous_cost = calculate_total_cost(year - 1, initial_cost, annual_maintenance_cost, efficiency_loss_rate, memo)
        maintenance_cost = annual_maintenance_cost * (1 + 0.02) ** year
        efficiency_loss = efficiency_loss_rate ** year
        cost = previous_cost + maintenance_cost - efficiency_loss

    memo[year] = cost
    return cost
