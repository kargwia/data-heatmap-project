import numpy as np
import pandas as pd

df=pd.read_csv("triple.csv")
a=df['a'].to_numpy()
b=df['b'].to_numpy()

n=len(a)

#means
mean_a=a.mean()
mean_b=b.mean()

#formula of cov:sum((a-mean_a)*(b-mean_b))/(n-1)
cov_ab=np.sum((a-mean_a)*(b-mean_b))/(n-1)

#standart auytqu
std_a=np.sqrt(np.sum((a-mean_a)**2)/(n-1))
std_b=np.sqrt(np.sum((b-mean_b)**2)/(n-1))

#corr
corr_ab=cov_ab/(std_a*std_b)

print("a and b cov and corr")
print(f"n={n}")
print(f"mean_a={mean_a:.4f}")
print(f"mean_b={mean_b:.4f}")
print(f"std_a={std_a:.4f}")
print(f"std_b={std_b:.4f}")
print(f"cov(a,b)={cov_ab:.4f}")
print(f"corr(a,b)={corr_ab:.4f}")
