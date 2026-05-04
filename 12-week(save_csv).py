import pandas as pd

df=pd.read_csv("triple.csv")

corr_matrix=df[['a','b','c']].corr()

print("corr matrix 3x3")
print(corr_matrix.round(6))

#save to csv
corr_matrix.to_csv("corr_matrix.csv")
print("\ncorr_matrix.csv saved")

check = pd.read_csv("corr_matrix.csv", index_col=0)
print("\nchecked-saved corr_matrix.csv:")
print(check.round(6))