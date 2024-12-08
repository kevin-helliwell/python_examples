import last_two


def test_last_two():
    list = [1, 2, 3, 4, 5]
    assert last_two.get_last_two(list) == [4, 5]
