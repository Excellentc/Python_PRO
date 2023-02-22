
"""
Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель",
наслідувані від "Транспортний засіб". Наповніть класи атрибутами на свій розсуд.
Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".
"""


def green_wiki(color_number="32"):
    def decorate(wiki_string_data):
        def _wrapper(*args, **kwargs):
            start_color = "\33[" + color_number + "m"
            end_color = "\33[0m"
            function_result = wiki_string_data(*args, **kwargs)
            color_wiki_string = start_color + function_result + end_color
            return color_wiki_string

        return _wrapper
    return decorate


class Vehicle:
    min_team = 1
    max_team = 80
    max_speed = 600

    @green_wiki()
    def short_information(self):
        wikipedia = "Device designed to transport people, goods or equipment installed on it."
        return wikipedia


class Car(Vehicle):
    application_area = "Earth"
    min_speed = 5

    @green_wiki("33")
    def short_information(self):
        wikipedia = f'Technical device that performs mechanical movements to convert energy and materials using \n' \
                    f'frictional force for movement Intended to transport people, goods or equipment installed on it\n' \
                    f'on roads. They may  achieve max speed over {self.max_speed} and moved by {self.application_area}'
        return wikipedia


class Airplane(Vehicle):
    application_area = "Air"
    min_speed = 90

    @green_wiki("34")
    def short_information(self):
        wikipedia = f'An aircraft designed to provide rapid transportation of people and goods using lift and \n'\
                    f'ascending/descending air streams. Not a single land and water transport can now move as fast\n' \
                    f'as an airplane. They may achieve max speed over {self.max_speed} kl/h and moved by ' \
                    f'{self.application_area}'
        return wikipedia


class Boat(Vehicle):
    application_area = "Water"
    min_speed = 5

    @green_wiki("35")
    def short_information(self):
        wikipedia = f'The ship is designed to ensure the transportation of people and goods by water using the laws \n' \
                    f'of Archimedes. They may achieve max speed over {self.max_speed} and moved by {self.application_area}'
        return wikipedia


air_vehicle = Airplane()
water_vehicle = Boat()
earth_vehicle = Car()
