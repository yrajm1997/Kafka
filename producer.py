### If an error occur, stating "No module named 'kafka.vendor.six.moves'" then try by uncommenting below lines.
# import six
# import sys
# if sys.version_info >= (3, 12, 0):
#     sys.modules['kafka.vendor.six.moves'] = six.moves

from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(bootstrap_servers ="localhost:29092")

for i in range (10):
    message = {"message": f"Hello, Kafka! {i}"}
    producer.send("test", json.dumps(message).encode("utf-8"))         # 'test' is the topic name
    time.sleep(random.randint(1,5))

producer.flush()
