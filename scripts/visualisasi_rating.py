import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Baca file rating dan movie
ratings = pd.read_csv('../data/ml-1m/ratings.csv')
movies = pd.read_csv('../data/ml-1m/movies.csv')

# Gabungkan data
movie_ratings = pd.merge(ratings, movies, on='movieId')

# Hitung jumlah rating per film
top_movies = movie_ratings['title'].value_counts().head(10)

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x=top_movies.values, y=top_movies.index, palette='viridis')
plt.title('🎬 10 Film Paling Sering Diberi Rating')
plt.xlabel('Jumlah Rating')
plt.ylabel('Judul Film')

# Simpan gambar
plt.tight_layout()
plt.savefig('../diagrams/top10_movies_rating.png')  # bisa disisipkan di laporan

print("✅ Grafik berhasil dibuat dan disimpan di: diagrams/top10_movies_rating.png")
