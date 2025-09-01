import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/ornek-veri.csv")

print(df.head())
print(df.describe())

plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="yas", y="maas")
plt.title("Yaş vs Maaş")
plt.show()
