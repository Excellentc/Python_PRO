import string
from functools import wraps
from random import choice, randint, random


def raise_invalid_input_data(func):
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
    We generate a floating point number. The output of the number is carried out modulo with a type change to 'int'
    """
    result = int(abs(random() * randint(-5 ** 5, 5 ** 5)))
    return result


@raise_invalid_input_data
def random_string_generation(string_len: int = 10) -> str:
    """
    We accept a value (string_len) of type 'int' and create a string variable in which the number
    of letters == string_len. All letters are lowercase.
    """
    generated_string = ''.join(choice(string.ascii_lowercase) for i in range(string_len))
    return generated_string
