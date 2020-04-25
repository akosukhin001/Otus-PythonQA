s1 = 'some string with spaces'


def test_1():
    assert s1.split(' ') == ['some', 'string', 'with', 'spaces']


def test_2():
    assert s1.islower()


def test_3():
    assert s1.isnumeric() == False


def test_4():
    assert s1.count('e') >= 2


def test_5(string_fixture):
    assert string_fixture in s1
