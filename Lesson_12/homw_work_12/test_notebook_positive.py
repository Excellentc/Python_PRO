def test_mobile_brand_type(notebook_device_positive):
    assert type(notebook_device_positive.brand) == str, 'Type result is incorrect'


def test_mobile_model_type(notebook_device_positive):
    assert type(notebook_device_positive.model) == str, 'Type result is incorrect'


def test_mobile_price_type(notebook_device_positive):
    assert type(notebook_device_positive.price) == float or int, 'Type result is incorrect'


def test_mobile_scr_size_type(notebook_device_positive):
    assert type(notebook_device_positive.screen_size) == str, 'Type result is incorrect'


def test_mobile_brand(notebook_device_positive):
    assert notebook_device_positive.brand == "HP", 'Value result is incorrect'


def test_mobile_model(notebook_device_positive):
    assert notebook_device_positive.model == "L34006", 'Value result is incorrect'


def test_mobile_price(notebook_device_positive):
    assert notebook_device_positive.price == 1100, 'Type result is incorrect'


def test_mobile_scr_size(notebook_device_positive):
    assert notebook_device_positive.screen_size == "15.2 inches", 'Value result is incorrect'


def test_mobile_get_short_info(notebook_device_positive):
    assert notebook_device_positive.get_short_info() == "HP L34006, 1100$, Screen Size: 15.2 inches", \
        "Short info incorrect"
