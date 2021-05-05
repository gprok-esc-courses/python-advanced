
def add_numbers(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        return 0


def add_many(*args):
    total = 0
    try:
        for v in args:
            total += int(v)
        return total
    except ValueError:
        return -1


def check_student(**kwargs):
    print(kwargs)


def some_function(a, b, *args, **kwargs):
    print(a, b, args, kwargs)


if __name__ == '__main__':
    some_function(3, 5, 6, 7, 8, value="A", purpose="test")
    some_function(1, 2, action="omit args")