from t10_tdd.mylib import *


def test_add_two_numbers():
    assert add_numbers(3, 5) == 8
    assert add_numbers("John", "Mary") == 0


def test_add_many():
    assert add_many(1, 2, 3) == 6
    assert add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 55
    assert add_many() == 0
    assert add_many(1, 2, 3, "5") == 11
    assert add_many(1, 2, 3, "John") == -1