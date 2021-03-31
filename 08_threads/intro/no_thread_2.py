from time import sleep


def counter(name):
    for i in range(5):
        print(name, ': ', i)
        sleep(4)
    print(name, ' complete')


def main():
    for name in ['A', 'B', 'C', 'D', 'E']:
        counter(name)
    print('ALL DONE')


if __name__ == '__main__':
    main()
