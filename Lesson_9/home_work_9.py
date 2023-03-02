
"""
Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель",
наслідувані від "Транспортний засіб". Наповніть класи атрибутами на свій розсуд.
Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".
"""
from abc import ABC, abstractmethod
from typing import Union


def color_wiki(color_number="32"):
    def decorate(wiki_string_data):
        def _wrapper(*args, **kwargs):
            start_color = "\33[" + color_number + "m"
            end_color = "\33[0m"
            function_result = wiki_string_data(*args, **kwargs)
            color_wiki_string = start_color + function_result + end_color
            return color_wiki_string

        return _wrapper
    return decorate


class Vehicle(ABC):

    def __init__(self, cruising_speed: Union[int, float], crew: int) -> None:
        self.crew = crew
        self.cruising_speed = cruising_speed

    @color_wiki()
    @abstractmethod
    def __str__(self):
        wikipedia = f"Device designed to transport people, goods or equipment installed on it. "
        return wikipedia

    __repr__ = __str__


class Car(Vehicle):

    def __init__(self, cruising_speed: Union[int, float], crew: int, application_area: str, max_speed: Union[int, float],
                 installing_weapon: bool, car_name: str) -> None:
        super().__init__(cruising_speed, crew)
        self.max_speed = max_speed
        self.installing_weapon = installing_weapon
        self.application_area = application_area
        self.car_name = car_name

    @color_wiki("33")
    def __str__(self):
        wikipedia = f'Technical device that performs mechanical movements to convert energy and materials using \n' \
                    f'frictional force for movement Intended to transport people, goods or equipment installed on it\n' \
                    f'on roads. They may  achieve max speed over {self.max_speed} kl/h and moved by {self.application_area}'
        return wikipedia

    __repr__ = __str__


class Airplane(Vehicle):

    def __init__(self, cruising_speed: Union[int, float], crew: int, application_area: str, max_speed: Union[int, float],
                 installing_weapon: bool, airplane_name: str) -> None:
        super().__init__(cruising_speed, crew)
        self.max_speed = max_speed
        self.installing_weapon = installing_weapon
        self.application_area = application_area
        self.airplane_name = airplane_name

    @color_wiki("34")
    def __str__(self):
        wikipedia = f'An aircraft designed to provide rapid transportation of people and goods using lift and \n' \
                    f'ascending/descending air streams. Not a single land and water transport can now move as fast\n' \
                    f'as an airplane. They may achieve max speed over {self.max_speed} kl/h and moved by ' \
                    f'{self.application_area}'
        return wikipedia

    __repr__ = __str__


class Boat(Vehicle):

    def __init__(self, cruising_speed: Union[int, float], crew: int, application_area: str, max_speed: Union[int, float],
                 installing_weapon: bool, boat_name: str, hold_volume: Union[int, float]) -> None:
        super().__init__(cruising_speed, crew)
        self.max_speed = max_speed
        self.installing_weapon = installing_weapon
        self.application_area = application_area
        self.boat_name = boat_name
        self.hold_volume = hold_volume

    @color_wiki("35")
    def __str__(self):
        if self.installing_weapon is True:
            self.weapon_info = "Equipped with anti-ship torpedoes and ground-to-air missiles for air defense"
        else:
            self.weapon_info = ""
        wikipedia = f'The ship is designed to ensure the transportation of people and goods by water using the\n' \
                    f'laws of Archimedes. They may achieve max speed over {self.max_speed} kl/h and moved by ' \
                    f'{self.application_area}.  \n{self.weapon_info}  '
        return wikipedia

    __repr__ = __str__


first_earth_vehicle = Car(250, 1, "Earth", 320, False, "Formula 1")
first_air_vehicle = Airplane(75.5, 3, "Air", 120, True, "Bomber")
first_water_vehicle = Boat(35, 1, "Water", 60, True, "Border boat", 5)
