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

    start = time.time()
    make_calculation_one(number_list)
    make_calculation_two(number_list)
    make_calculation_three(number_list)
    end = time.time()

    print(end - start)
