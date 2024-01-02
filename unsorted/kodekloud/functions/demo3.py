def my_function(*argv):
    print(argv[0])


my_function('Hello', 'World!')


def my_function(*argv):
    print(argv)


my_function('Hello', 'World!')


def my_function(arg1, *argv):
    print("First argument:", arg1)
    for arg in argv:
        print("Next argument:", arg)


my_function('Welcome', 'to', 'Python!')
