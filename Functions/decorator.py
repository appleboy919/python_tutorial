def f1(f):
    def f2():
        print('this is before the function call')
        f()
        print('this is after the function call')
    return f2


@f1         # f1 takes f3 as an argument, returns and assigned that name of f3
def f3():
    print('this is f3')


# x = f1  # make x as a function
# x()     # calls f2()

# cannot call f2() directly, bcs f2 only exists inside the scope of f1
# f1 is a wrapper for f2
# f2()

# x = f1(f3)
# x()
f3 = f1(f3)  # f3 is now a decorator (f1 as a wrapper function)
f3()

# Note
# 1: Decorator is a form of metaprogramming (special type of function), returning a wrapper function
# 2: In Python, everything, including functions, are objects
