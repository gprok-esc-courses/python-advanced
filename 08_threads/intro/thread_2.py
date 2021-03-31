import threading
import random
from time import sleep


def counter(name):
    for i in range(5):
        print(name + ': ' + str(i) + '\n', end='')
        sleep(random.randint(1, 5))
    print(name + ' complete\n', end='')


def main():
    for name in ['A', 'B', 'C', 'D', 'E']:
        t = threading.Thread(target=counter, args=(name,))
        t.start()
    print('ALL DONE')


if __name__ == '__main__':
    main()
