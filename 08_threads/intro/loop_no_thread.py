from time import sleep, ctime


def action0():
    print('start action0 at:', ctime())
    sleep(10)
    print('action0 done at:', ctime())


def action1():
    print('start action1 at:', ctime())
    sleep(2)
    print('action1 done at:', ctime())


def main():
    print('starting at:', ctime())
    action0()
    action1()
    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
