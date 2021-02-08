a = 4
b = 5
# x = 'three {} {}'.format(4, 5)
# x = 'three {1} {0}'.format(4, 5)
# x = 'three "{1:>04}" "{0:<04}"'.format(4, 5)
x = f'three {a:<4} {b:>4}'  # fstring
print('x is {}'.format(x))
print(type(x))

### NOTE ###
# 1: fstring is available after python 3.6
