def class1():
    print('this is class1...')
    # return 'ret_value'
    # return [12, 13, 14]
    return dict(x=1, y=2, z=3)


x = class1()
print('return value:', x)
print(type(x))
