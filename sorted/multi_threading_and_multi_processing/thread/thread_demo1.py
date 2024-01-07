import threading
import time

done = False


def worker(text):
    counter = 0
    while counter < 30:
        time.sleep(1)
        counter += 1
        print(f"Thread {threading.current_thread().name}, ")
        print(f"{text}: counter = {counter}, ")


# threading.Thread(target=worker, daemon=True, args=("ABC",)).start()
# threading.Thread(target=worker, daemon=False, args=("XYZ",)).start()

t1 = threading.Thread(target=worker, daemon=True, args=("ABC",))
t2 = threading.Thread(target=worker, daemon=False, args=("XYZ",))

t1.start()
t2.start()

t1.join()
t2.join()

input("Press enter to quit\n")
print(f"Thread {threading.current_thread().name}")
done = True
