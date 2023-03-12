"""створити ієрархію класів
    (реалізувати наслідування) гаджетів
    (наприклад, телефон та ноутбук зі спільним абстрактним предком)
    створити фікстури відповідних сутностей та покрити їх тестами
"""
from abc import ABC, abstractmethod


class Gadget(ABC):
    def __init__(self, brand: str, model: str, price: int | float) -> None:
        self.brand = brand
        self.model = model
        self.price = price

    def get_short_info(self):
        return f"{self.brand} {self.model}, {self.price}$"

    @abstractmethod
    def get_additional_info(self):
        wikipedia = f"Gadget - a small device designed to facilitate and improve life. "
        return wikipedia


class Mobile(Gadget):
    def __init__(self, brand: str, model: str, price: int | float, os: str) -> None:
        if not isinstance(brand, str):
            raise TypeError("Brand must be a string")
        if not isinstance(model, str):
            raise TypeError("Model must be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be an integer or float")
        if not isinstance(os, str):
            raise TypeError("OS must be a string")
        super().__init__(brand=brand, model=model, price=price)
        self.os = os

    def get_short_info(self):
        return f"{super().get_short_info()}, OS: {self.os}"

    def get_additional_info(self):
        wikipedia = f"Mobile phone - a phone designed to work in cellular networks; uses a radio band transceiver " \
                    f"and traditional telephone switching to carry out telephone communications within the " \
                    f"territory of the cellular network coverage area. "
        return wikipedia


class Notebook(Gadget):
    def __init__(self, brand: str, model: str, price: int | float, screen_size: str) -> None:
        if not isinstance(brand, str):
            raise TypeError("Brand must be a string")
        if not isinstance(model, str):
            raise TypeError("Model must be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be an integer or float")
        if not isinstance(screen_size, str):
            raise TypeError("Screen size must be a string")
        super().__init__(brand=brand, model=model, price=price)
        self.screen_size = screen_size

    def get_short_info(self):
        return f"{super().get_short_info()}, Screen Size: {self.screen_size}"

    def get_additional_info(self):
        wikipedia = f"Notebook (English notebook - notepad) - a portable computer, with the ability connect " \
                    f"to the Internet both via cable and via WI-FI module "
        return wikipedia
