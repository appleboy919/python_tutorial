

def main():
    # x = [5] (list)
    x = 5
    y = x
    print("id of x in main:", id(x))
    print("id of y in main:", id(y))
    kitten(x)
    print(f"in main: x is {x}")


def kitten(a):
    print("id of a in kitten()", id(a))
    # a[0] = 3 --> "in main: x is 3"
    a = 3
    print("after assigning 3 in kitten", id(a))
    print("Meow")
    print("a in kitten:", a)


if __name__ == "__main__":
    main()

### Note ###
# 1: integers are immutable (like in Java)
# 2: mutable objects such as lists can be changed
# ==> "CALL BY REFERENCE"
