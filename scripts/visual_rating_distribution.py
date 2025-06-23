import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data ratings
ratings = pd.read_csv('../data/ml-1m/ratings.csv')

# Plot distribusi rating
plt.figure(figsize=(8, 5))
sns.countplot(data=ratings, x='rating', palette='Set2')

plt.title('Distribusi Rating Film')
plt.xlabel('Rating')
plt.ylabel('Jumlah')
plt.tight_layout()

# Simpan ke file
plt.savefig('../diagrams/distribusi_rating.png')
plt.show()

print("✅ Visualisasi distribusi rating berhasil disimpan di diagrams/distribusi_rating.png")
