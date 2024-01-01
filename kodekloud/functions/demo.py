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
