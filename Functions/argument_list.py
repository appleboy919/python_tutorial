def arg_list(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print("Empty list")


def kwarg_func(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('{}, {}'.format(k, kwargs[k]))
    else:
        print('empty dictionary')


arg_list(1, 2, 3)
x = (1, 3, 5, 7)
y = []
arg_list(*x)
arg_list(*y)

kwarg_func(one='1', two='2', three='3')
a = {'4': 'four', '5': 'five', '6': 'six'}
kwarg_func(**a)
kwarg_func()
