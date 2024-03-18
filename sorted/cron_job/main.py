import schedule
import time
import threading


def scheduled_job():
    print("This is a scheduled job")


def job():
    print(f"Current thread name: {threading.current_thread().getName()}")
    print("This is a scheduled job")


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


def scheduled_job():
    print(f"Current thread name: {threading.current_thread().getName()}")
    print("I'm working...")


if __name__ == "__main__":
    # 1.
    # while True:
    #     scheduled_job()
    #     time.sleep(5)

    # 2.
    # while True:
    #     run_threaded(job)
    #     time.sleep(5)

    # 3. schedule
    # schedule.every(10).seconds.do(job)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(2)


    # 4. Python Crontab
    
    # 5. Python-rq, a tool leveraging Redis as a broker, facilitates job queuing. 
    
    # 6. airflow
    
    pass
    