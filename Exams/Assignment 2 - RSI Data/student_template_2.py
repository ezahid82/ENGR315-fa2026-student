"""
CULMINATING ASSIGNMENT 2: RSI

Create a program which will provide answers to the tasks posed in the assignment description.

For this assignment, you will start from scratch with this blank template.
It is your reponsibility to include all necessary program components in this file.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.

The relevant data file is named "all_participant_data_rsi.csv" and is located in data > drop-jump.

All file paths need to be relative and execute from this file's directory;
the Visual Studio Code setting "Python > Terminal: Execute in File Dir" 
must be enabled in File > Preferences > Settings.

See Canvas for additional requirements.
"""
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


#making a path
file_path = "../../data/drop-jump/all_participant_data_rsi.csv"
df = pd.read_csv(file_path)

print(df.info())
print(df.head(), "\n")

#Task 1:

print("TASK 1: Paired t-Test Ananlysis")


forcePlate_rsi = df["force_plate_rsi"]
accelRsi = df["accelerometer_rsi"]

#doing a relative ttest
t_stat, p_value = stats.ttest_rel(forcePlate_rsi, accelRsi)

#printing out initial hypotheses
print("Null Hypothesis (H_0): The Mean difference between methods is zero.")
print("Alternative Hypothesis (Ha): The Mean difference is non-zero.")
print(f"Calculated t-value: {t_stat:.4f}")
print(f"Calculated p-value: {p_value: .4f}")

#cheching our hypotheses
alpha = 0.05
if p_value < alpha:
    print("Conclusion: We reject the null hypothesis, because of a significant"
    " difference detected between the methods.")
else:
    print("Conclusion: We fail to reject the null hypothesis, because" 
        " there was no significant difference detected between the methods.")


# Task 2:

print("TASK 2: Chi-Square Goodness of Fit Test (Accelerometer RSI)")

#getting the mean and stdev
mu, std = stats.norm.fit(accelRsi)
print(f"Fitted Normal Distribution -> Mean (mu): {mu:.4f}, Std (std): {std:.4f}")
num_bars = 10

#starting to make our histogram
counts, bar_edges = np.histogram(accelRsi, bins=num_bars, density=False)
cdf_edges = stats.norm.cdf(bar_edges, loc=mu, scale=std)
expected_probs = np.diff(cdf_edges)
expected_counts = expected_probs * len(accelRsi)
expected_counts = expected_counts * (counts.sum() / expected_counts.sum())

#getting the chi-2 and p value
chi2_stat, chi2_p_value = stats.chisquare(f_obs=counts, f_exp=expected_counts)

print(f"Chi2 Statistic: {chi2_stat:.4f}")
print(f"p-value: {chi2_p_value:.4e}")

#checking our conclusion
if chi2_p_value > alpha:
  print(
      "Conclusion: Good fit! The accelerometer RSI data follows a normal"
      " distribution." )
else:
   print("Conclusion: Poor fit. The data deviates significantly from a normal"
        " distribution.")


#plotting the historgam in vs code.
   plt.figure(figsize=(8, 5))
plt.hist(
    accelRsi, bins=num_bars, density=True, alpha=0.6, color="g", label="Data Histogram"
)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mu, std)
plt.plot(x, p, "k", linewidth=2, label="Normal Fit PDF")
plt.title("Accelerometer RSI Distribution Fit", fontsize=14, fontweight="bold")
plt.xlabel("Reactive Strength Index (RSI)", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.legend(loc="upper right")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("accelerometer_rsi_normal_fit.png")
plt.show()
print("Plot saved as 'accelerometer_rsi_normal_fit.png'\n")
