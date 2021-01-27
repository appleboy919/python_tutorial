from decimal import *
x = .1 + .1 + .1 - .3  # in a real world, this should be zero
print('x is {}'.format(x))  # not actually zero (almost zero)
print(type(x))

# use modules for accuracy
a = Decimal('.10')
b = Decimal('.30')
y = a + a + a - b
print('y is {}'.format(y))
print(type(y))


# note
# 1: float type --> sacrificing accuracty for precision
# 2: DO NOT USE FLOAT FOR ACCURACY  ex) Money
