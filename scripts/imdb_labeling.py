import os
import pandas as pd

def load_imdb_data(base_path):
    data = []

    for label_type in ['pos', 'neg']:
        label = 1 if label_type == 'pos' else 0
        for subset in ['train', 'test']:
            path = os.path.join(base_path, subset, label_type)

            # Pastikan foldernya ada
            if not os.path.exists(path):
                print(f"⚠️ Folder tidak ditemukan: {path}")
                continue

            for file in os.listdir(path):
                file_path = os.path.join(path, file)

                # Lewati jika bukan file .txt
                if not file_path.endswith(".txt"):
                    continue

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        data.append((content, label))
                except Exception as e:
                    print(f"❌ Gagal membaca file: {file_path}\n{e}")

    df = pd.DataFrame(data, columns=['review', 'label'])
    return df

# Path dataset IMDb
base_path = '../data/aclImdb'

# Output path
output_path = os.path.join(base_path, 'imdb_reviews_labeled.csv')

# Proses dan simpan
imdb_df = load_imdb_data(base_path)
imdb_df.to_csv(output_path, index=False)

print(f"✅ Review IMDb berhasil diberi label dan disimpan di: {output_path}")
