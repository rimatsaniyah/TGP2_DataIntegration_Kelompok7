import pandas as pd
import re
from nltk.corpus import stopwords
import nltk

# Download stopwords (tidak pakai punkt lagi)
nltk.download('stopwords', quiet=True)

# Load review IMDb yang sudah diberi label
df = pd.read_csv('../data/aclImdb/imdb_reviews_labeled.csv')

# Preprocessing function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'<.*?>', '', text)                # hapus tag HTML
    text = re.sub(r'[^a-z\s]', '', text)             # hapus angka dan simbol
    words = text.split()                             # split manual
    stop_words = set(stopwords.words('english'))     # ambil stopwords
    filtered = [word for word in words if word not in stop_words]
    return ' '.join(filtered)

# Terapkan ke semua review
df['cleaned_review'] = df['review'].apply(clean_text)

# Simpan ke CSV
df.to_csv('../data/aclImdb/imdb_reviews_cleaned.csv', index=False)

print("✅ Preprocessing selesai! File disimpan di: imdb_reviews_cleaned.csv")
