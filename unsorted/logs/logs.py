import logging
import json
from datetime import datetime
import calendar
import random
import threading
import time

# Set up logging
logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format='%(message)s')

# Function to put logs into the stream
def put_to_stream(id, value, timestamp):
    payload = {
        'random': str(value),
        'timestamp': str(timestamp),
        'id': id
    }
    response = json.dumps(payload)
    logging.debug(response)

# Function to generate and write 1000 random logs
def write_logs(thread_id):
    for _ in range(1000):
        value = random.randint(1, 100)
        timestamp = calendar.timegm(datetime.utcnow().timetuple())
        id = 'user-' + str(random.randint(1, 10))
        put_to_stream(id, value, timestamp)

# Continuously write logs every xx seconds
while True:
    # Create and start 10 threads
    threads = []
    for i in range(10):
        thread = threading.Thread(target=write_logs, args=(i,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Wait for seconds before writing logs again
    time.sleep(30)
