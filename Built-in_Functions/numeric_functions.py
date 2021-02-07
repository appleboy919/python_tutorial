x = '47'
y = int(x)
z = float('-32.2')
absZ = abs(z)
divMod = divmod(y, 3)
comp1 = y + 17j
comp2 = complex(y, 3)

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')
print(f'z is {type(z)}')
print(f'z is {z}')
print(f'absZ is {type(absZ)} {absZ}')
print(f'divMod is {type(divMod)} {divMod}')
print(f'divMod is {type(comp1)} {comp1}')
print(f'divMod is {type(comp2)} {comp2}')
