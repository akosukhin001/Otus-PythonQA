import pytest


@pytest.fixture(params=[45, 'str', ('tpl',)])
def list_fixture(request):
    return request.param


@pytest.fixture(params=[1, 2, 3])
def set_fixture(request):
    return request.param


@pytest.fixture(params=['value2', 'value3', 'value4'])
def dict_fixture(request):
    return request.param


@pytest.fixture(params=['some', 'str', 'tabulation'])
def string_fixture(request):
    return request.param
