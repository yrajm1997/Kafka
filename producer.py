### If an error occur, stating "No module named 'kafka.vendor.six.moves'" then try by uncommenting below lines.
# import six
# import sys
# if sys.version_info >= (3, 12, 0):
#     sys.modules['kafka.vendor.six.moves'] = six.moves

from kafka import KafkaProducer
import json, time, random

import tweepy

# Twitter API credentials
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAJyMzgEAAAAAtP5d2gVC0hrEXxJNDCPEbRKglig%3Dc2y9l0DESel8bLAYlzlus4VZz9up5W7LbAUg53VMnfOthG6R8Y"

producer = KafkaProducer(bootstrap_servers ="localhost:9092")

# Authenticate Twitter API
client = tweepy.Client(bearer_token=BEARER_TOKEN)
def fetch_tweets():
    query = "#AI OR #Tech -is:retweet"  # Search for tweets with these hashtags, excluding retweets
    tweets = client.search_recent_tweets(query=query, tweet_fields=["created_at", "text", "id"], max_results=10)
    if tweets.data:
        for tweet in tweets.data:
            tweet_data = {
                "id": tweet.id,
                "text": tweet.text,
                "timestamp": str(tweet.created_at)
            }
            producer.send("twitter-stream", value=tweet_data)  # Send to Kafka
            print(f"Tweet sent: {tweet_data}")
# Run every 30 seconds to fetch new tweets
while True:
    fetch_tweets()
    time.sleep(30)  # Wait before fetching again


#for i in range (10):
#while True:
#    message = input("Enter message here: ") #{"message": f"Hello, Kafka! {i}"}
#    producer.send("test", json.dumps(message).encode("utf-8"))         # 'test' is the topic name
#    time.sleep(random.randint(1,5))

producer.flush()
