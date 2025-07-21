def calculate_net_gain_and_percentage_gain(initial_portfolio_value, final_portfolio_value, initial_net_deposits, final_net_deposits):
    # Net Gain Calculation
    net_gain = final_portfolio_value - (initial_portfolio_value + (final_net_deposits - initial_net_deposits))

    # Percentage Gain Calculation
    percentage_gain = (net_gain / (initial_portfolio_value + (final_net_deposits - initial_net_deposits))) * 100

    return net_gain, percentage_gain

# Example data
initial_portfolio_value = 24370.03
final_portfolio_value = 26135.02
initial_net_deposits = 24161.60
final_net_deposits = 25213.49

# Calculate Net Gain and Percentage Gain
net_gain, percentage_gain = calculate_net_gain_and_percentage_gain(initial_portfolio_value, final_portfolio_value, initial_net_deposits, final_net_deposits)

print(f"Net Gain: {net_gain}")
print(f"Percentage Gain: {percentage_gain:.2f}%")
