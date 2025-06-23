import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data IMDb yang sudah diberi label
imdb = pd.read_csv('../data/aclImdb/imdb_reviews_labeled.csv')

# Plot distribusi sentimen
plt.figure(figsize=(6, 5))
sns.countplot(data=imdb, x='label', palette='coolwarm')
plt.xticks([0, 1], ['Negatif', 'Positif'])

plt.title('Distribusi Sentimen Review IMDb')
plt.xlabel('Sentimen')
plt.ylabel('Jumlah Review')
plt.tight_layout()

plt.savefig('../diagrams/sentimen_review_imdb.png')
plt.show()

print("✅ Visualisasi sentimen berhasil disimpan di diagrams/sentimen_review_imdb.png")
