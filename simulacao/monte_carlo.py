import numpy as np

def monte_carlo_simulation(num_simulations, num_years, initial_cost, inflation_rate, maintenance_cost, energy_conversion_efficiency):
    simulations = []

    for _ in range(num_simulations):
        total_cost = initial_cost
        costs = [initial_cost]

        for year in range(1, num_years + 1):
            inflation = np.random.normal(loc=inflation_rate, scale=0.01)
            maintenance = np.random.normal(loc=maintenance_cost, scale=0.01)
            efficiency_loss = np.random.normal(loc=energy_conversion_efficiency, scale=0.01)

            annual_cost = total_cost * (1 + inflation) + maintenance - efficiency_loss
            costs.append(annual_cost)
            total_cost += annual_cost

        simulations.append(costs)

    return simulations
