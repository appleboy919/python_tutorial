def main():
    for i in inclusive_range(5):
        print(i, end=' ')
    print('')

    for i in inclusive_range(1, 4):
        print(i, end=' ')
    print('')

    for i in inclusive_range(1, 10, 2):
        print(i, end=' ')
    print('')

# generator which works as an inclusive range function


def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    # initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:
        yield i
        i += step


if __name__ == '__main__':
    main()

# Note
# 1: Generator is a special class of function that serves as an iterator (returns stream of values)
# 2: Having more than 2 arguemtns, use (arg1, arg2, ...) = list_args
# 3: yield --> return keyword for Generators
