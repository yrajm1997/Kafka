# Kafka
To learn and test Kafka with Python

Steps to follow:

1. Start a Codespace
2. Create a virtual environment: `python -m venv venv`
3. Activate virtual environment: `source venv/bin/activate`
4. Install requirements: `pip install -r requirements.txt`
5. Start Kafka using docker by running this command: `docker-compose up -d`
6. Run consumer python script to make consumer ready to receive messages: `python consumer.py`
7. Start one more terminal, and activate virtual environment in it
8. In this 2nd terminal, run producer python script to send messages: `python producer.py`
9. Now, check the 1st terminal, messages should be received at the consumer end
10. Once done, stop Kafka by running this command: `docker-compose down`
