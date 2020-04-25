my_dict = {2: 'value1', 3: 'value2', 5: 'value3'}


def test_1():
    assert repr(my_dict.items()) == "dict_items([(2, 'value1'), (3, 'value2'), (5, 'value3')])"


def test_2():
    assert my_dict[3] == 'value2'


def test_3():
    assert my_dict.get(2) == my_dict[2]


def test_4():
    my_dict2list = list(my_dict)
    assert my_dict2list == [2, 3, 5]


def test_5(dict_fixture):
    assert dict_fixture in my_dict.values()
