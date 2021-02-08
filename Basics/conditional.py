def main():
    x, y = 10, 100

    st = "none"
    # conditional flow uses if, elif, else
    if(x < y):
        st = "x is less than y"
    elif(x == y):
        st = "x is the same as y"
    else:
        st = "x is greater than y"

    print(st)

    # conditional statements let you use "a if C else b"
    st = "x is less than y" if (
        x < y) else "x is greater than or the same as y"

    print(st)

    # A is B
    a = 1
    b = 1
    if a is b:
        print('a is b')
    else:
        print('a is not b')
    
    # a is in A
    A = [1,2,3,4]
    if 1 in A:
        print('1 is in A')
    else:
        print('1i is not in A')


if __name__ == "__main__":
    main()


# note
# 1 there's no equivalent switch conditional in Python
