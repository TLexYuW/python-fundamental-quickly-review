import logging
import json
from datetime import datetime
import calendar
import random
import threading
import time
import uuid

# Set up logging
logging.basicConfig(filename='file.log', level=logging.DEBUG, format='%(message)s')

# Function to put logs into the stream
def put_to_stream(id, v1, v2, timestamp):
    payload = {
        'random': str(v1),
        'random2': str(v2),
        'timestamp': str(timestamp),
        'uid': id
    }
    response = json.dumps(payload)
    
    # Check if this log data has already been generated
    if response not in generated_logs:
        generated_logs.add(response)
        logging.debug(response)

# Function to generate and write unique random logs
def write_logs(thread_id):
    while len(generated_logs) < 100000:
        v1 = uuid.uuid4()
        v2 = uuid.uuid4()
        timestamp = calendar.timegm(datetime.utcnow().timetuple())
        id = 'user-' + str(random.randint(1, 10))
        put_to_stream(id, v1, v2, timestamp)

# Run the script continuously
while True:
    # Set to store generated log data for this iteration
    generated_logs = set()

    # Create and start 10 threads to generate logs
    threads = []
    for i in range(10):
        thread = threading.Thread(target=write_logs, args=(i,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Ensure the log file has exactly 100,000 lines
    while len(generated_logs) < 100000:
        v1 = uuid.uuid4()
        v2 = uuid.uuid4()
        timestamp = calendar.timegm(datetime.utcnow().timetuple())
        id = 'user-' + str(random.randint(1, 10))
        put_to_stream(id, v1, v2, timestamp)

    # Sleep for x minute before the next iteration
    time.sleep(60)
