# TGP2 Data Integration Kelompok 7

## 📌 **Deskripsi Proyek**

Proyek ini bertujuan untuk **mengintegrasikan data rating film (MovieLens) dengan data sentimen ulasan film (IMDb)** menggunakan pipeline data end-to-end. Proses mencakup ingestion data dengan Apache Kafka, transformasi dan analisis data dengan Apache Spark, penyimpanan data menggunakan PostgreSQL, serta **visualisasi insight menggunakan Apache Superset**.

## 🗂️ **Dataset**

* **MovieLens 1M**
  [https://grouplens.org/datasets/movielens/1m/](https://grouplens.org/datasets/movielens/1m/)
* **IMDb Large Movie Review Dataset**
  [https://ai.stanford.edu/\~amaas/data/sentiment/](https://ai.stanford.edu/~amaas/data/sentiment/)

## 🔨 **Tools & Library**

* **Apache Kafka** (Data ingestion)
* **Apache Spark (PySpark)** (Data processing & anomaly detection)
* **PostgreSQL** (Database penyimpanan data)
* **Apache Superset** (Visualisasi data interaktif)
* **Docker & Docker Compose** (Containerization)
* **Python** (pandas, pyspark, kafka-python, nltk)
* **Git & GitHub** (Version control)

## 🔁 **Alur Proses**

1️⃣ **Ingestion Data dengan Kafka**
* Mengirim dataset MovieLens (setelah dikonversi dari `.dat` ke `.csv`) dan dataset IMDb ke Kafka topic.

2️⃣ **Preprocessing & Transformasi Data dengan Spark**
* Labeling dan preprocessing teks IMDb untuk sentimen positif/negatif.
* Menggabungkan dataset rating dan sentimen menggunakan Spark SQL.
* Analisis prediksi rating film dan deteksi anomaly rating-review.

3️⃣ **Penyimpanan ke PostgreSQL**
* Data hasil transformasi disimpan ke PostgreSQL sebagai data mart.

4️⃣ **Visualisasi Data dengan Superset**
* Membuat dashboard insight menggunakan Superset dengan koneksi ke PostgreSQL untuk monitoring dan analisis visual.

## 📊 **Hasil Visualisasi pada Superset**
Insight yang divisualisasikan:
* **Jumlah Film yang Diprediksi**
* **10 Film dengan Selisih Prediksi Terjauh**
* **Data Prediksi Film (Top 10 dan Lengkap)**
* **Top 10 Film Berdasarkan Rating dan Reviews**
* **Jumlah Film dengan Anomali Rating Rendah Review Bagus**
* **Genre Anomali Rating Rendah Review Bagus Terbanyak**
* **Jumlah Film dengan Anomali Rating Tinggi Review Jelek**
* **Genre Anomali Rating Tinggi Review Jelek Terbanyak**

Visualisasi ini membantu tim memahami distribusi genre, evaluasi akurasi prediksi, serta identifikasi film dengan potensi rekomendasi sesuai ulasan pengguna.
