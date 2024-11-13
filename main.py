from simulacao import monte_carlo_simulation
from comparacao import compare_sources
from memoization import calculate_total_cost
from tarifas import simulate_tariff_growth

# Parâmetros de exemplo para a simulação de Monte Carlo
num_simulations = 1000
num_years = 30
initial_cost = 50000
inflation_rate = 0.02
maintenance_cost = 500
energy_conversion_efficiency = 0.9

simulations = monte_carlo_simulation(num_simulations, num_years, initial_cost, inflation_rate, maintenance_cost, energy_conversion_efficiency)
print("Simulações de Monte Carlo concluídas.")

# Dados de exemplo para a comparação de fontes
costs_catracas = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490]
costs_paineis = [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590]

comparison = compare_sources(costs_catracas, costs_paineis)
print("Comparação de fontes concluída.")

# Exemplo de uso de memoization
for year in range(31):
    total_cost = calculate_total_cost(year, initial_cost, maintenance_cost, energy_conversion_efficiency)
    print(f"Ano {year}: Custo total = {total_cost:.2f}")

# Exemplo de simulação de crescimento de tarifas
initial_tariff = 0.05  # Tarifa inicial em reais por kWh
increment_rate = 0.03  # Taxa de incremento anual

for year in range(31):
    tariff = simulate_tariff_growth(year, initial_tariff, increment_rate)
    print(f"Ano {year}: Tarifa de energia = {tariff:.4f} R$/kWh")
