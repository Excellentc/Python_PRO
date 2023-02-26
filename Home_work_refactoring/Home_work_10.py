import string
from functools import wraps
from random import choice, randint, random


def check_invalid_input_data(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        values = [*args]
        for value in values:
            if not isinstance(value, int):
                raise TypeError('I have got not a number')
            if value < 0:
                raise ValueError('Entering a negative value')
        result = func(*args, **kwargs)
        return result

    return _wrapper


def get_random_number() -> int:
    """
    Function generate a floating point number. Number output is modulo with type change to 'int'
    Returns: int

    """
    result = int(abs(random() * randint(-5 ** 5, 5 ** 5)))
    return result


@check_invalid_input_data
def random_string_generation(string_len: int = 10) -> str:
    """
    Function accepts values(string_len) of 'int' type and creates a string variable, in which number of
    letters == string_len. All letters are lowercase.
    Args:
        string_len: int
    By default string_len == 10
    Returns: string

    """
    generated_string = ''.join(choice(string.ascii_lowercase) for i in range(string_len))
    return generated_string


get_random_number()
random_string_generation(20)
random_string_generation(get_random_number())
