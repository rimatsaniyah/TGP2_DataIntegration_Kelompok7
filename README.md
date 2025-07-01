# TGP2 Data Integration Kelompok 7

## 📌 Deskripsi Proyek
Proyek ini bertujuan mengintegrasikan data rating film (MovieLens) dengan data sentimen ulasan film (IMDb) menggunakan pipeline data integration end-to-end berbasis **Apache Kafka, MinIO, Apache Spark, Hive, PostgreSQL, dan Apache Superset**. Proses mencakup ingestion, penyimpanan, pembersihan, transformasi, analisis sederhana, dan visualisasi insight.

## 🗂️ Dataset
- **MovieLens 1M:** [https://grouplens.org/datasets/movielens/1m/](https://grouplens.org/datasets/movielens/1m/)
- **IMDb Large Movie Review Dataset:** [https://ai.stanford.edu/~amaas/data/sentiment/](https://ai.stanford.edu/~amaas/data/sentiment/)

## 🔨 Tools & Library
- **Apache Kafka** (message broker untuk ingestion)
- **MinIO** (object storage sebagai datalake)
- **Apache Spark (Python)** (pembersihan dan transformasi data)
- **Apache Hive** dan **PostgreSQL** (data warehouse dan metadata)
- **Apache Superset** (visualisasi data & pembuatan dashboard)
- Python libraries: pandas, pyspark, nltk, matplotlib, seaborn

## 🔁 Alur Proses
1️⃣ Konversi file `.dat` MovieLens ke `.csv` untuk ingestion.  
2️⃣ Labelisasi sentimen review IMDb (positif/negatif) menggunakan NLTK.  
3️⃣ Ingestion data MovieLens dan IMDb menggunakan Kafka.  
4️⃣ Penyimpanan data mentah ke **MinIO** sebagai datalake.  
5️⃣ Spark membaca data dari MinIO untuk dilakukan **preprocessing dan transformasi**.  
6️⃣ Data hasil transformasi disimpan ke Hive Table di HDFS, metadata dikelola PostgreSQL.  
7️⃣ Visualisasi dan eksplorasi insight menggunakan **Apache Superset** yang terhubung ke Hive Server.

## 🖼️ Visualisasi Dashboard Superset
Dashboard Superset menampilkan insight berikut:
- Jumlah Film yang Diprediksi
- 10 Film dengan Selisih Terjauh
- Data Prediksi Film (10)
- Data Prediksi Lengkap
- Top 10 Film Berdasarkan Rating dan Reviews
- Jumlah Film dengan Anomali Rating Rendah Review Bagus
- Genre dengan Anomali Rating Rendah Review Bagus (Total dan Per Genre)
- Jumlah Film dengan Anomali Rating Tinggi Review Jelek
- Genre dengan Anomali Rating Tinggi Review Jelek (Total dan Per Genre)

