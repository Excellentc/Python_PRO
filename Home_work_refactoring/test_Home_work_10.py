import Home_work_10 as Lib
import pytest

test_cases_get_random_string_generation = [
    False,
    2,
    50000000,
    0,
    1.5,
    [],
    -1,
    "str",
    None,
]
test_cases_get_random_string_length = [
    0,
    1,
    1234567,
    435,
    -1
]


def test_get_random_number():
    assert type(Lib.get_random_number()) == int, 'Type result is incorrect'


@pytest.mark.parametrize("number", test_cases_get_random_string_generation)
def test_random_string_generation(number):
    assert type(Lib.random_string_generation(number)) is str, 'Type result is incorrect'


@pytest.mark.parametrize('number', test_cases_get_random_string_length)
def test_random_string_generation_check_string_length(number):
    assert len(Lib.random_string_generation(number)) == number, 'Length of the string is different from the ' \
                                                                'desired length'


def test_random_string_generation_with_random_number():
    assert type(Lib.random_string_generation(Lib.get_random_number())) is str, 'Type result is incorrect'
