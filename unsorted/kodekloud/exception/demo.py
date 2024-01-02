# try:
#     test = 1
#     print("test = " + tes)
# except:
#     print("Errrrrrr")


# print("Done")


# try:
#     x = int(input("Enter a number: "))
#     y = 1 / x
#     print(y)

# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except ValueError:
#     print("ValueError")
# except:
#     print("Else Wrong")


# print("Done")


# try:
#     print("my_string"[1/0])
# except IndexError:
#     print("index error")
# except ZeroDivisionError:
#     print("zero error")
# except:
#     print("other error")

# try:
#       x = y + 1
# except NameError:
#       print("y is not defined")


try:
    x = 'seasalt'[7]
except IndexError:
    print("No character found in that index")
