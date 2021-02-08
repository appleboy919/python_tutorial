import sys
import os
import random
import datetime


def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    print('Platform: {}'.format(sys.platform))
    print('OS name: {}'.format(os.name))

    # os module
    env_path = os.getenv('PATH')
    print(env_path)
    cwd = os.getcwd()
    print(cwd)
    # 25 bytes long random number in hexadecimal
    ran_num = os.urandom(25).hex()
    print(ran_num)

    # random module
    x = random.randint(1, 1000)
    print(x)
    ran_list = list(range(25))
    print(ran_list)
    random.shuffle(ran_list)
    print(ran_list)

    # datetime module
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.microsecond)


if __name__ == '__main__':
    main()
