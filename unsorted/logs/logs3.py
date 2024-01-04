import logging
import json
from datetime import datetime
import calendar
import random
import threading
import time
import uuid
import pytz

# Set up logging
logging.basicConfig(filename='file.log', level=logging.DEBUG, format='%(message)s')

# Function to put logs into the stream
def put_to_stream(id, v1, v2, timestamp):
    # Convert the timestamp from UTC to TW timezone
    utc_timezone = pytz.timezone('UTC')
    tw_timezone = pytz.timezone('Asia/Taipei')
    utc_time = datetime.utcfromtimestamp(timestamp).replace(tzinfo=utc_timezone)
    tw_time = utc_time.astimezone(tw_timezone)

    payload = {
        'random': str(v1),
        'random2': str(v2),
        'timestamp': tw_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'),
        'uid': id
    }
    response = json.dumps(payload)

    # Check if this log data has already been generated
    if response not in generated_logs:
        generated_logs.add(response)
        logging.debug(response)

# Function to generate and write unique random logs
def write_logs(thread_id):
    while len(generated_logs) < 100_000:
        v1 = uuid.uuid4()
        v2 = uuid.uuid4()
        timestamp = calendar.timegm(datetime.utcnow().timetuple())
        id = 'user-' + str(random.randint(1, 10))
        put_to_stream(id, v1, v2, timestamp)

# Main loop to generate logs every 5 minutes
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

    # Sleep for x minutes before the next iteration
    time.sleep(60)
