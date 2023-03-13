import pytest
from library import Mobile, Notebook


@pytest.fixture(scope='class')
def mobile_device_positive():
    mobile_data = Mobile(
        brand="Apple",
        model="iPhone 6",
        price=250.5,
        os="iOS",
    )
    yield mobile_data


@pytest.fixture(scope='class')
def notebook_device_positive():
    notebook_data = Notebook(
        brand="HP",
        model="L34006",
        price=1100,
        screen_size="15.2 inches")
    yield notebook_data


@pytest.fixture(scope='class')
def mobile_device_negative():
    mobile_data = Mobile(
        brand=123,
        model=6,
        price="250",
        os=14,
    )
    yield mobile_data


@pytest.fixture(scope='class')
def notebook_device_negative():
    notebook_data = Notebook(
        brand=23.4,
        model=[1],
        price="1100",
        screen_size=15.2)
    yield notebook_data
