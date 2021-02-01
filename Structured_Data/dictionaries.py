def print_dict(o):
    for x in o:
        print(f'{x}: {o[x]}')


numbers = {'1': 'one', '2': 'two', '3': 'three'}
print(numbers)
print_dict(numbers)

# use dict() constructor (for string-keys)
nums = dict(one='1', two='2', three='3')
print(nums)
print_dict(nums)

# key and value pairs
for k, v in nums.items():
    print(f'({k}, {v})')

# only keys
for k in nums.keys():
    print(k)

# only values
for v in nums.values():
    print(v)

# access to a value
print(nums['one'])
nums['one'] = '1one1'
print(nums['one'])
print('found two!' if 'two' in nums else 'No two...')
print(nums.get('four'))
