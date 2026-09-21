"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $33B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
Note that Elon's capital will be $33B.
"""

### all your code below ###


elon_capital = 33000000000 # initial capital in dollars
ten_year_rate = 3.96 # interest rate for 10-year bonds in percent
twenty_year_rate = 4.32 # interest rate for 20-year bonds in percent
ten_year_calc = elon_capital * (1 + ten_year_rate/100)**10 # A = P(1 + r/n)^(nt)
twenty_year_calc = elon_capital * (1 + twenty_year_rate/100)**20 # A = P(1 + r/n)^(nt)

# final answer for 10-year
ten_year_final = ten_year_calc # final value of the investment after 10 years
print("10-year final value:", ten_year_final) # printing final value

# final answer for 20-year
twenty_year_final = twenty_year_calc # final value of the investment after 20 years
print("20-year final value:", twenty_year_final) # printing final value