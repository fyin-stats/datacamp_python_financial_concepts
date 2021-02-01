##################
##################
# https://learn.datacamp.com/courses/introduction-to-financial-concepts-in-python
##################
##################

# Course objectives
# the time value of money
# compound interest
# discounting and projecting cashflows
# making rational economic decisions
# mortgage structures
# interest and equity
# the cost of capital
# wealth accumulation


# calculating return on investment
# cumulative growth (or deprecation)

# Investment value = v_t0 * (1+r)^t
# growth rate is hard to predict

# Discount factors
# df = 1/(1+r)^t
# future value * discount factor = initial value
# Compound interest
# Investment value = v_t0 * (1 + r/c)^(t*c)
# number of compounding periods

# Exponential growth
# Compounded quarterly
# Compounded annually
#

# Compound interest
#
# As you saw in the previous exercise, both time and the rate of return are very
# important variables when forecasting the future value of an investment.
#
# Another important variable is the number of compounding periods,
# which can greatly affect compounded returns over time.

# Predefined variables
initial_investment = 100
growth_periods = 30
growth_rate = 0.06

# Calculate the value for the investment compounded once per year
compound_periods_1 = 1
investment_1 = initial_investment*(1 + growth_rate / compound_periods_1)**(compound_periods_1*growth_periods)
print("Investment 1: " + str(round(investment_1, 2)))

# Calculate the value for the investment compounded quarterly
compound_periods_2 = 4
investment_2 = initial_investment*(1 + growth_rate / compound_periods_2)**(compound_periods_2*growth_periods)
print("Investment 2: " + str(round(investment_2, 2)))

# Calculate the value for the investment compounded monthly
compound_periods_3 = 12
investment_3 = initial_investment*(1 + growth_rate / compound_periods_3)**(compound_periods_3*growth_periods)
print("Investment 3: " + str(round(investment_3, 2)))


#
# Calculate the future value
initial_investment = 100
growth_rate = -0.05
growth_periods = 10
future_value = initial_investment*(1 + growth_rate)**(growth_periods)
print("Future value: " + str(round(future_value, 2)))

# Calculate the discount factor
discount_factor = 1/((1 + growth_rate)**(growth_periods))
print("Discount factor: " + str(round(discount_factor, 2)))

# Derive the initial value of the investment
initial_investment_again = future_value * discount_factor
print("Initial value: " + str(round(initial_investment_again, 2)))



# Present and future value
# The non-static value of money
# situation 1
# Option A: $100 in your pocket today
# Option B: $100 in your pocket tomorrow

# situation
# Option A: $10000 today
# Option B: $10500 next year

# Comparing future values
# on average, can quantify the payout
#

import numpy as np
# calculate the present value of $100 received 3 years from now
# at a 1.0% inflation rate
np.pv(rate = 0.01, nper = 3, pmt = 0, fv = 100)

# future value in python, $100 invested for 3 years at a 5.0% average annual rate of return
# negative sign represents cash flow out (i.e., money not available today)
np.fv(rate = 0.05, nper = 3, pmt = 0, pv=-100) # negative value means you
# are spending money now

# calculate future value
import numpy as np

# Calculate investment_1
investment_1 = np.fv(rate=0.05, nper=15, pmt=0, pv = -10000)
print("Investment 1 will yield a total of $" + str(round(investment_1, 2)) + " in 15 years")

# Calculate investment_2
investment_2 = np.fv(rate=0.08, nper = 15, pmt = 0, pv = -10000)
print("Investment 2 will yield a total of $" + str(round(investment_2, 2)) + " in 15 years")


#
# Adjusting future values for inflation
#
# You can now put together what you learned in the previous exercises by following a simple methodology:
#
#     First, forecast the future value of an investment given a rate of return
#     Second, discount the future value of the investment by a projected inflation rate
#
# The methodology above will use both the .fv() and .pv() functions to arrive at the projected
# value of a given investment in today's dollars, adjusted for inflation.


# Net present value
# and cash flows
# cash flows are a series of gains or losses from an investment over time
# Project 1 cashflows, project 2 cashflows
# assume a 3% dicsount rate
# sum of all present values together
#

# arrays in numpy
# Net present value
# np.npv, calculates the present value of a given cashflow
#

# Diminishing cash flows
#
# Remember how compounded returns grow rapidly over time? Well, it works in the reverse, too. Compounded discount factors over time will quickly shrink a number towards zero.
#
# For example, $100 at a 3% annual discount for 1 year is still worth roughly $97.08:
#
# But this number shrinks quite rapidly as the number of discounting periods increases:
#
# This means that the longer in the future your cash flows will be received (or paid), the close to 0 that number will be.
#
#


# Comparing project NPV with IRR
#
