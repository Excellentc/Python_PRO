import library as lib
import pytest

test_cases_get_random_string_generation = [
    False,
    2,
    50000000,
    0,
]
test_cases_get_random_string_length = [
    0,
    1,
    1234567,
    435,
]
test_cases_get_negative_data_for_raise_type_error = [
    1.5,
    "str",
    None,
]
test_case_get_negative_data_for_raise_value_error = [
    -1,
]


def test_get_random_number():
    assert type(lib.get_random_number()) == int, 'Type result is incorrect'


@pytest.mark.parametrize("number", test_cases_get_random_string_generation)
def test_random_string_generation(number):
    assert type(lib.random_string_generation(number)) is str, 'Type result is incorrect'


@pytest.mark.parametrize('number', test_cases_get_random_string_length)
def test_random_string_generation_check_string_length(number):
    assert len(lib.random_string_generation(number)) == number, 'Length of the string is different from the ' \
                                                                'desired length'


def test_random_string_generation_with_random_number():
    assert type(lib.random_string_generation(lib.get_random_number())) is str, 'Type result is incorrect'


@pytest.mark.parametrize('number', test_case_get_negative_data_for_raise_value_error)
def test_random_string_generation_error_value(number):
    with pytest.raises(ValueError):
        assert lib.random_string_generation(number)


@pytest.mark.parametrize('number', test_cases_get_negative_data_for_raise_type_error)
def test_random_string_generation_error_type(number):
    with pytest.raises(TypeError):
        assert lib.random_string_generation(number)
