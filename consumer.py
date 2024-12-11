from kafka import KafkaConsumer

consumer = KafkaConsumer("test", bootstrap_servers ="localhost:29092", auto_offset_reset="earliest")    # 'test' is the topic name

for message in consumer:
    print ( message.value.decode("utf-8"))
    