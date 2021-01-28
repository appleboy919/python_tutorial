x = [1, 2, 3, 4]  # list is created with [] brackets
x[0] = 0  # list is mutable
for i in x:
    print("i is {}".format(i))

y = (1, 2, 3, 4)  # tuple is created with () parentheses
for j in y:
    print("j is {}".format(j))
y[0] = 0  # this line is an error -> tuple is immutable

### NOTE ###
# 1: List is mutable -> can reassign
