from kafka import KafkaProducer
import csv
import json
import time

producer = KafkaProducer(
    bootstrap_servers=['localhost:29092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    api_version=(3, 2, 3)
)

topic_name = 'raw-csv'

with open('data/coba.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        # Optional: konversi tipe data ke int biar JSON nya lebih clean
        row['movieId'] = int(row['movieId'])
        row['imdbId'] = int(row['imdbId'])
        row['tmdbId'] = int(row['tmdbId'])
        
        producer.send(topic_name, value=row)
        print(f"Sent to Kafka: {row}")
        time.sleep(0.5)

producer.flush()
producer.close()
