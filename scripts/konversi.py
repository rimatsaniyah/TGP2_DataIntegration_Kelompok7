import pandas as pd

# Path ke folder .dat kamu
base_path = '../data/ml-1m/'

# Konversi movies.dat
movies = pd.read_csv(base_path + 'movies.dat', sep='::', engine='python',
                     names=['MovieID', 'Title', 'Genres'], encoding='latin-1')
movies.to_csv(base_path + 'movies.csv', index=False)

# Konversi ratings.dat
ratings = pd.read_csv(base_path + 'ratings.dat', sep='::', engine='python',
                      names=['UserID', 'MovieID', 'Rating', 'Timestamp'], encoding='latin-1')
ratings.to_csv(base_path + 'ratings.csv', index=False)

# Konversi users.dat
users = pd.read_csv(base_path + 'users.dat', sep='::', engine='python',
                    names=['UserID', 'Gender', 'Age', 'Occupation', 'Zip-code'], encoding='latin-1')
users.to_csv(base_path + 'users.csv', index=False)

print("✅ Konversi selesai! Cek file .csv di folder data/ml-1m/")
