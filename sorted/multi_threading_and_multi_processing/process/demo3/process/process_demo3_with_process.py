import multiprocessing as mp
import math
import time

results_a = []
results_b = []
results_c = []


def make_calculation_one(nums):
    for num in nums:
        results_a.append(math.sqrt(num**3))


def make_calculation_two(nums):
    for num in nums:
        results_b.append(math.sqrt(num**4))


def make_calculation_three(nums):
    for num in nums:
        results_c.append(math.sqrt(num**5))


if __name__ == "__main__":
    number_list = list(range(50_000_000))

    p1 = mp.Process(target=make_calculation_one, daemon=False, args=(number_list,))
    p2 = mp.Process(target=make_calculation_two, daemon=False, args=(number_list,))
    p3 = mp.Process(target=make_calculation_three, daemon=False, args=(number_list,))

    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    end = time.time()

    print(end - start)
