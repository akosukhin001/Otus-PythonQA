set_from_list = set([1, 2, 3, 5, 7, 2, 1, ])
set_from_list2 = set([1, 'sth', 4.5])
set_from_string = set('some string w/ spaces')
set_from_string2 = set('some string w/ spaces')


def test_1():
    assert {x for x in range(1, 4)}.issubset(set_from_list)


def test_2():
    assert set_from_list.intersection(set_from_list2) == {1}


def test_3():
    u = set_from_list.union(set_from_list2)
    assert u - set_from_list2 == set_from_list.difference(set_from_list2)


def test_4():
    assert set_from_string.discard('s') == set_from_string2.remove('s')


def test_5(set_fixture):
    assert set_fixture in set_from_list
