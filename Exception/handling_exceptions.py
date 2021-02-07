import sys


def main():
    print('Hello, World.')
    try:
        # x = int('foo')
        x = 5/0
    except ValueError:
        print('Caught ValueError!')
    # except ZeroDivisionError:
    #     print('No / with 0')
    except:
        print(f'unknown error: {sys.exc_info()[1]}')
    else:
        print('No Error!')
        print(x)


if __name__ == '__main__':
    main()

 ### Note ###
 # try -> except ___Error -> except -> else (NO Errors)
 # use sys.exc_info()[1] for details about an error
