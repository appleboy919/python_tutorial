def main():
    x = 0

    # define a while loop
    print("while loop")
    while(x < 5):
        print(x)
        x = x+1
    print("")

    # define a for loop
    print("for loop")
    for x in range(5, 10):
        print(x)
    print("")

    # use a for loop over a collection
    print("collection for loop")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)
    print("")

    # use the break and continue statements
    for x in range(5, 10):
        if(x == 7):
            break
        if(x % 2 == 0):
            continue
        print(x)
    print("")

    # using the enumerate() function to get index
    print("using enumerate() function")
    for i, d in enumerate(days):
        print(i, d)


if __name__ == "__main__":
    main()

# Note
# Python only has 2 loop sturctures: while, for
# Loops are like iterators in Python
# enumerate() function returns the index of the item
