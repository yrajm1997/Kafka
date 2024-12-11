# Kafka
To learn and test Kafka with Python

Steps:

1. Start a Codespace
2. Run : `docker-compose up -d`
3. Create python environment: `python -m venv venv`
4. Activate python environment: `source venv/bin/activate`
5. Install requirements: `pip install -r requirements.txt`
6. Have 2 terminals ready
7. In 1st terminal, run consumer script to receive messages: `python consumer.py`
8. In 2nd terminal, run producer script to send messages: `python producer.py`
9. Check the 1st terminal, messages should be reeived at consumer end

