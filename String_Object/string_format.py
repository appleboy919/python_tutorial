x = 42
y = 73

# string interpolation
print('the number is {} {}'.format(x, y))
print('numbers: {xx} {bb}'.format(xx=x, bb=y))
print('numbers: {0} {1} {0}'.format(x, y))

# order formatting ':' '+' ',' '._f'
print('numbers: {0:<5}. {1:>5}'.format(x, y))
print('numbers: {0:<5}. {1:>+05}'.format(x, y))
print('{:,}'.format(x*y*1298).replace(',', '.'))
print('number is {:.3f}'.format(x*y))
print('hexadecimal: {:o}\tbinary:{:b}'.format(x, x))

# F string formatting
print(f'the number is {x:.3f}')
