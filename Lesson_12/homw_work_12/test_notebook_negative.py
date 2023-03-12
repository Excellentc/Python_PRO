def test_notebook_brand_type(notebook_device_negative):
    assert type(notebook_device_negative.brand) != str, 'Type result is incorrect'


def test_notebook_model_type(notebook_device_negative):
    assert type(notebook_device_negative.model) != str, 'Type result is incorrect'


def test_notebook_price_type(notebook_device_negative):
    assert type(notebook_device_negative.price) != int or float, 'Type result is incorrect'


def test_notebook_scr_size_type(notebook_device_negative):
    assert type(notebook_device_negative.screen_size) != str, 'Type result is incorrect'


def test_notebook_brand(notebook_device_negative):
    assert notebook_device_negative.brand != "HP", 'Value result is incorrect'


def test_notebook_model(notebook_device_negative):
    assert notebook_device_negative.model != "L34006", 'Value result is incorrect'


def test_notebook_price(notebook_device_negative):
    assert notebook_device_negative.price == 1100, 'Value result is incorrect'


def test_notebook_scr_size(notebook_device_negative):
    assert notebook_device_negative.screen_size != "15.2 inches", 'Value result is incorrect'
