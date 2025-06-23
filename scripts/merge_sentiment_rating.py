import pandas as pd

# Load MovieLens data
movies = pd.read_csv('../data/ml-1m/movies.csv', sep=',')
ratings = pd.read_csv('../data/ml-1m/ratings.csv', sep=',')

# Load IMDb cleaned reviews
reviews = pd.read_csv('../data/aclImdb/imdb_reviews_cleaned.csv')

# Gabungkan ratings dengan movie titles
movie_ratings = pd.merge(ratings, movies, on='movieId')

# Contoh: Ambil film populer (banyak rating)
popular_movies = movie_ratings['title'].value_counts().head(10)
print("🎬 10 Film paling sering diberi rating:")
print(popular_movies)

# Coba cocokkan salah satu judul dengan sentimen review IMDb
# Misal: "Toy Story (1995)" → keyword: "toy story"
keyword = "toy story"
matched_reviews = reviews[reviews['cleaned_review'].str.contains(keyword.lower(), na=False)]

print(f"\n📝 Review IMDb dengan kata kunci '{keyword}': {len(matched_reviews)} review ditemukan")
print("Distribusi Sentimen:")
print(matched_reviews['label'].value_counts())

# Tambahan opsional: Simpan hasil ke CSV
matched_reviews.to_csv(f'../data/aclImdb/{keyword.replace(" ", "_")}_reviews_subset.csv', index=False)

print("\n✅ Merge & analisis sederhana selesai!")
