from kafka import KafkaConsumer

import json
import pandas as pd
from transformers import pipeline
import os


consumer = KafkaConsumer("twitter-stream", bootstrap_servers ="localhost:9092", auto_offset_reset="earliest")    # 'test' is the topic name

#for message in consumer:
#   print(message.value.decode("utf-8"))


# Load Hugging Face Sentiment Model
sentiment_pipeline = pipeline("sentiment-analysis")

CSV_FILE = "tweet_sentiment.csv"

count = 1

for message in consumer:
    message = message.value.decode("utf-8")
    sentiment = sentiment_pipeline(message)[0]
    result = {
        "tweet_id": count,
        "tweet": message.strip('"'),
        "sentiment": sentiment["label"],
        "sentiment_score": round(sentiment["score"], 3)
    }
    count += 1

    print(f"Processed: {result}")

    # Write to CSV immediately
    df = pd.DataFrame([result])
    df.to_csv(CSV_FILE, mode="a", header=not os.path.exists(CSV_FILE), index=False)
    print("Saved to CSV")

