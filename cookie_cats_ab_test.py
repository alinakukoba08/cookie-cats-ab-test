import pandas as pd
from scipy.stats import chi2_contingency
import math

df = pd.read_csv("data/cookie_cats.csv")

# Group analysis
summary = df.groupby("version")[["retention_1", "retention_7"]].mean()
print(summary)

# Chi-square test
table_1 = pd.crosstab(df["version"], df["retention_1"])
table_7 = pd.crosstab(df["version"], df["retention_7"])

chi2_1, p1, _, _ = chi2_contingency(table_1)
chi2_7, p7, _, _ = chi2_contingency(table_7)

print("Day 1 p-value:", p1)
print("Day 7 p-value:", p7)

# Confidence interval
def ci(p, n):
    z = 1.96
    se = math.sqrt((p * (1 - p)) / n)
    return (p - z * se, p + z * se)

for v in ["gate_30", "gate_40"]:
    subset = df[df["version"] == v]
    p = subset["retention_7"].mean()
    n = len(subset)
    print(v, ci(p, n))
