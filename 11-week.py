import numpy as np
import pandas as pd

df = pd.read_csv("triple.csv")

#pandas corr matrix
corr_matrix = df[['a', 'b', 'c']].corr()
print("Pandas .corr() matrix")
print(corr_matrix.round(6))

#comparing with 10th task
a = df['a'].to_numpy()
b = df['b'].to_numpy()
n = len(a)
mean_a, mean_b = a.mean(), b.mean()
std_a = np.sqrt(np.sum((a - mean_a) ** 2) / (n - 1))
std_b = np.sqrt(np.sum((b - mean_b) ** 2) / (n - 1))
cov_ab = np.sum((a - mean_a) * (b - mean_b)) / (n - 1)
corr_ab_manual = cov_ab / (std_a * std_b)

pandas_ab = corr_matrix.loc['a', 'b']

print("\ncompare: corr(a,b) ")
print(f"qolmen eseptelgen: {corr_ab_manual:.10f}")
print(f"pandas .corr(): {pandas_ab:.10f}")
print(f"difference: {abs(corr_ab_manual - pandas_ab):.2e}")
print("same results" if abs(corr_ab_manual - pandas_ab) < 1e-9 else "difference")