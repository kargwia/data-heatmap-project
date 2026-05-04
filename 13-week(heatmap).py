import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("triple.csv")
corr_matrix=df[['a','b','c']].corr()

fig,ax=plt.subplots(figsize=(7,6))

sns.heatmap(
    corr_matrix,
    annot=True,#numvers on cell
    fmt=".3f",#3 ondyq
    cmap="YlGn",#green color
    vmin=-1, vmax=1,
    linewidths=0.8,
    linecolor="white",
    annot_kws={"size": 14, "weight": "bold"},
    ax=ax
)

ax.set_title("corr matrix(a,b,c)",fontsize=16,fontweight="bold",pad=15)
ax.set_xticklabels(['a','b','c'],fontsize=13)
ax.set_yticklabels(['a','b','c'],fontsize=13,rotation=0)

plt.tight_layout()
plt.savefig("heatmap.png",dpi=150, bbox_inches="tight")
print("✓ heatmap.png сақталды!")
plt.show()