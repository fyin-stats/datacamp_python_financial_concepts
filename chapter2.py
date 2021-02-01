#######################
#######################
# Common profitability analysis methods
#######################
#######################


# Net present value: NPV is equal to the sum of all discounted cash flows
# Ct: cash flow C at time t
# r: Discount rate
# NPV is a simple cashflow valuation measure that does not allow for
# the comparison of differenct sized projects or lengths
#


# Internal rate of return (IRR): solve NPV = 0
# IRR can be used to compare projects of different sizes
# and lengths but requires an algorithmic solution and
# does not measure total value
# IRR: percentage

# pip install numpy-financial
import numpy as np
import numpy_financial as npf

project_1 = np.array([-100, 150, 200]) # requires an initial investment of value 100
# np.irr(project_1)
npf.irr(project_1)
# 1.35

# the weighted average cost of capital (WACC)
# use WACC to discount values
# WACC = F_Equity * C_Equity + F_Debt * C_Debt * (1-TR)
# F_Equity: The proportion of a company's financing via equity
# F_Debt: The proportion of a company's financing via debt
# C_Equity: The cost of a company's equity
# C_Debt: the cost of a company's debt
# TR: the corporate tax rate

# Proportion of financing can be calculated as follows:
# F_Equity = M_Equity / M_Total
# F_Debt = M_Debt / M_Total
# M_Total = M_Debt + M_Equity
# M_Debt : Market value of a company's debt
# M_Equity : Market value of a company's equity
# M_total : Market value of a company's financing

# Discounting using WACC
#
# Set the market value of debt
mval_debt = 1000000

# Set the market value of equity
mval_equity = 1000000

# Compute the total market value of your company's financing
mval_total = mval_debt + mval_equity

# Compute the proportion of your company's financing via debt
percent_debt = mval_debt / mval_total
print("Debt Financing: " + str(round(100*percent_debt, 2)) + "%")

# Compute the proportion of your company's financing via equity
percent_equity = mval_equity / mval_total
print("Equity Financing: " + str(round(100*percent_equity, 2)) + "%")

#
# The proportion of debt vs equity financing is predefined
percent_debt = 0.50
percent_equity = 0.50

# Set the cost of equity
cost_equity = 0.18

# Set the cost of debt
cost_debt = 0.12

# Set the corporate tax rate
tax_rate = 0.35

# Calculate the WACC
wacc = cost_equity * percent_equity + cost_debt * percent_debt * (1 - tax_rate)
print("WACC: " + str(round(100*wacc, 2)) + "%")


# Companies use their WACC as the discount rate when calculating the net present value of potential projects.
#
# In the same way that you discounted values by inflation in the previous chapter to account for costs over time, companies adjust the cash flows of potential projects by their cost of financing (the WACC) to account for their investor's required rate of return based on market conditions.
#
# Now that you calculated the WACC, you can determine the net present value (NPV) of each project's cash flows. The cash flows for projects 1 and 2 are available as cf_project1 and cf_project2.


# Comparing two projects of different life spans
# project comparison
# Assume a 5% discount rate for both projects
# Different NPVs and IRRs

# equivalent annual annuity (EAA) can be used to compare two projects
# of different lifespans in present value terms
# Apply the EAA method to the previous two projects using the computed
# NPVs * -1

import numpy as np

# Calculate the EAA for Project 1
eaa_project1 = np.pmt(rate=wacc, nper=8, pv=-1*npv_project1, fv=0)
print("Project 1 EAA: " + str(round(eaa_project1, 2)))

# Calculate the EAA for Project 2
eaa_project2 = np.pmt(rate=wacc, nper=7, pv=-1*npv_project2, fv=0)
print("Project 2 EAA: " + str(round(eaa_project2, 2)))