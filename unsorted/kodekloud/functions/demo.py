# def input_num():
#     return int(input("Enter a number: "))

# num = input_num()
# print(num)


def multi_func(num1, num2):
    return num1 * num2


res = multi_func(num2=5, num1=10)
print(res)


def my_function(*students):
    print("The tallest student is " + students[2])


my_function("James", "Ella", "Jackson")


def print_info(name, age=18):
    print(name, age)


print_info("john", 19)


def my_function(x):
    return 10 / x


print(my_function(2))


def get_odd_func(numbers):
    odd_numbers = []
    for num in numbers:
        if num % 2:
            odd_numbers.append(num)
    return odd_numbers


print(get_odd_func([7, 4, 5, 6, 9, 8, 12]))

def double_list(numbers):
  return 2 * numbers

numbers = [1, 2, 3]
print(double_list(numbers))
