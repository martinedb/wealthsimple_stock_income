# Wealthsimple Stock Income Analysis

This repository provides Python scripts to analyze stock portfolio performance on Wealthsimple, a popular Canadian investment platform. These scripts are designed to help investors understand their monthly and overall gains or losses, factoring in net deposits. While the examples use Wealthsimple, the methodology can be adapted for other banking or fintech platforms that allow investments in stocks and ETFs.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Scripts](#scripts)
  - [Monthly Gain/Loss Calculation](#monthly-gainloss-calculation)
  - [General Net Gain & Percentage Gain Calculation](#general-net-gain--percentage-gain-calculation)
- [Usage](#usage)
- [Adapting to Other Platforms](#adapting-to-other-platforms)
- [Requirements](#requirements)
- [License](#license)
- [Contributing](#contributing)

---

## Overview

Tracking portfolio performance accurately requires accounting for additional deposits and withdrawals. The scripts in this repository help you:

- Calculate how much you actually gained or lost in a given month, after accounting for net deposits.
- Calculate your overall net gain and percentage gain for any time period.

## Features

- **Monthly performance tracking:** Isolate gains or losses from new deposits.
- **General net and percentage gain calculation:** Works for any time period and can be reused for different investment platforms.
- **Simple Python code:** Easy to understand and modify for your own needs.

## Scripts

### 1. Monthly Gain/Loss Calculation

This script calculates the net gain (or loss) for a single month, taking into account any deposits made during that period. This helps you see your true investment performance, rather than being skewed by added funds.

**Example:**

```python
# Given data for the month
starting_portfolio_value = 26947.23
starting_net_deposits = 26613.28

ending_portfolio_value = 27454.46
ending_net_deposits = 28146.63

# Calculate net deposits during the month
net_deposits_during_month = ending_net_deposits - starting_net_deposits

# Calculate net gain
net_gain = (ending_portfolio_value - starting_portfolio_value) - net_deposits_during_month

print(f"Net gain/loss for the month: {net_gain:.2f}")
```

**How it works:**

- `starting_portfolio_value` and `ending_portfolio_value`: Your total portfolio value at the start and end of the month.
- `starting_net_deposits` and `ending_net_deposits`: The cumulative total of all deposits up to the start and end of the month.
- The script calculates how much was deposited during the month, then isolates the gain/loss attributable to investment performance only.

---

### 2. General Net Gain & Percentage Gain Calculation

This script lets you measure overall net gain (and percentage gain) for any period, adjusting for deposits. It's designed to be flexible for different platforms and timeframes.

**Example:**

```python
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

print(f"Net Gain: {net_gain:.2f}")
print(f"Percentage Gain: {percentage_gain:.2f}%")
```

**How it works:**

- Calculates true gain or loss by subtracting the effect of new deposits during the period.
- Calculates the percentage gain relative to the actual invested capital.

---

## Usage

1. **Obtain your values:** Export your portfolio values and net deposits from Wealthsimple (or your chosen platform) for the relevant dates.
2. **Run the scripts:** Replace the example values in the scripts with your own data.
3. **View your results:** The net gain/loss and percentage gain will be printed out.

## Adapting to Other Platforms

These scripts are not limited to Wealthsimple. You can adapt them to any brokerage, bank, or fintech platform if you have access to:

- Portfolio value at specific points in time
- Cumulative net deposits at those points

Simply plug in your own numbers to the provided functions.


## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for details.

*Created by [martinedb](https://github.com/martinedb)*
