list_one = [22, 15, 'something_new', 4.5]
list_two = [1, 'abc', (23, 'rs')]


def test_1():
    assert list(reversed(list_one)) == list_one[::-1]


def test_2():
    # assert ', '.join(map(str, list_one)) == '22, 15, something_new, 4.5'
    assert ', '.join(str(value) for value in list_one) == '22, 15, something_new, 4.5'


def test_3():
    assert list_one * 2 == [22, 15, 'something_new', 4.5, 22, 15, 'something_new', 4.5]


def test_4():
    list_two.pop(0)
    assert list_one + list_two == [22, 15, 'something_new', 4.5, 'abc', (23, 'rs')]


def test_5(list_fixture):
    l1_length = len(list_one)
    list_one.append(list_fixture)
    l2_length = len(list_one)
    assert l2_length == l1_length + 1
