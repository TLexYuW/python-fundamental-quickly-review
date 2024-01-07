import time

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
    append_list(1, 50_000_000)
    append_list(2, 50_000_000)
    append_list(3, 50_000_000)
    end = time.time()

    print(end - start)
