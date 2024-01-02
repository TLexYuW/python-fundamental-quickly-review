a = input("Enter a number: ")
try:
    float(a) / 0
except (TypeError, ZeroDivisionError):
    print("Please enter valid numbers, besides zero.")
