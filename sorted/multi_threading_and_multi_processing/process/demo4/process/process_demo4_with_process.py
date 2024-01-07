import time
import multiprocessing as mp


list_1 = []
list_2 = []
list_3 = []


def append_list(p, r):
    for x in range(r):
        list_1.append(x)
        list_2.append(x)
        list_3.append(x)
    print(f"{p} process completed!")


if __name__ == "__main__":
    start = time.time()
    p1 = mp.Process(
        target=append_list,
        args=(
            1,
            50_000_000,
        ),
    )
    p2 = mp.Process(
        target=append_list,
        args=(
            2,
            50_000_000,
        ),
    )
    p3 = mp.Process(
        target=append_list,
        args=(
            3,
            50_000_000,
        ),
    )
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    end = time.time()

    print(end - start)
