from order_numbers import order_numbers, sum_numbers,get_first_number


def test_order_numbers():
    assert order_numbers([1, 2, 3]) == [1, 2, 3]
    assert order_numbers([3, 2, 1]) == [1, 2, 3]

def test_sum_numbers():
    assert sum_numbers([1, 2, 3]) == 6
    assert sum_numbers([3, 2, 1]) == 6


def test_get_first_number():
    assert get_first_number([1, 2, 3]) == 1
   