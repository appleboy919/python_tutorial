def arg_list(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print("Empty list")


arg_list(1, 2, 3)
x = (1, 3, 5, 7)
y = []
arg_list(*x)
arg_list(*y)
