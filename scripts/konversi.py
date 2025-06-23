import pandas as pd

# Konversi ratings.dat
ratings = pd.read_csv('../data/ml-1m/ratings.dat', sep='::', engine='python',
                      names=['userId', 'movieId', 'rating', 'timestamp'],
                      encoding='latin-1')
ratings.to_csv('../data/ml-1m/ratings.csv', index=False)

# Konversi movies.dat
movies = pd.read_csv('../data/ml-1m/movies.dat', sep='::', engine='python',
                     names=['movieId', 'title', 'genres'],
                     encoding='latin-1')
movies.to_csv('../data/ml-1m/movies.csv', index=False)

# Konversi users.dat (opsional)
users = pd.read_csv('../data/ml-1m/users.dat', sep='::', engine='python',
                    names=['userId', 'gender', 'age', 'occupation', 'zipCode'],
                    encoding='latin-1')
users.to_csv('../data/ml-1m/users.csv', index=False)

print("✅ Konversi berhasil! Semua file .dat telah diubah ke .csv")
