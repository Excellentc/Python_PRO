str = 2  # this is just a piece of code to refactor and test
# you have fix codestyle (I will check it using flake8), write add typehinting, rename objects if it is necessary
# I will use mypy as well
# you have to fix functions if they work in incorrect way
# write documentation
# remember about namings, especially builtins
# you have to add tests (check errors, types and different values)  and manage its location
# the main idea of this homework - write readable and maintainable code
# function that are called directly here nust be moved to special main file
# it is not a joke - sometimes I receive this kind of code in homeworks
# do not forget about requirements.txt
from typing import Union
import string
from random import choice
def get_random_number():
    # this beautiful function generate integer number according to the fake documentation to provide you
    # the best service of generating totally random number
    # enjoy your random integer
    import random as some_module
    return some_module.random() * some_module.randint(-10**10, 10**10)

def random_strichka_generation(len: Union[float, int]=10):
    'генеруємо довільну стрічку заданої довжини і ніколи не отримуємо помилок'
    return ''.join(choice(string.ascii_lowercase) for i in range(len))

def test():
    assert type(random_strichka_generation()) == str


random_strichka_generation(20.)
random_strichka_generation(-1)


