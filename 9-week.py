import numpy as np
import pandas as pd

df = pd.read_csv("triple.csv")
matrix = df[['a', 'b', 'c']].to_numpy()

print("bastapqy matrix (algashqy 5 jol):")
print(matrix[:5])

col_means = matrix.mean(axis=0)
print(f"\nbagan ortashalary: a={col_means[0]:.2f}, b={col_means[1]:.2f}, c={col_means[2]:.2f}")

centered = matrix - col_means

print("\ncentered matrix(algashqy 5jol):")
print(centered[:5])

print("\ntekseru- ortalyqtangannan keyingi ortasha(0-ge jaqyn boluy kerek):")
print(centered.mean(axis=0).round(10))