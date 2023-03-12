def test_mobile_brand_type(mobile_device_positive):
    assert type(mobile_device_positive.brand) == str, 'Type result is incorrect'


def test_mobile_model_type(mobile_device_positive):
    assert type(mobile_device_positive.model) == str, 'Type result is incorrect'


def test_mobile_price_type(mobile_device_positive):
    assert type(mobile_device_positive.price) == float, 'Type result is incorrect'


def test_mobile_os_type(mobile_device_positive):
    assert type(mobile_device_positive.os) == str, 'Type result is incorrect'


def test_mobile_brand(mobile_device_positive):
    assert mobile_device_positive.brand == "Apple", 'Value result is incorrect'


def test_mobile_model(mobile_device_positive):
    assert mobile_device_positive.model == "iPhone 6", 'Value result is incorrect'


def test_mobile_price(mobile_device_positive):
    assert mobile_device_positive.price == 250.5, 'Value result is incorrect'


def test_mobile_os(mobile_device_positive):
    assert mobile_device_positive.os == "iOS", 'Value result is incorrect'


def test_mobile_get_short_info(mobile_device_positive):
    assert mobile_device_positive.get_short_info() == "Apple iPhone 6, 250.5$, OS: iOS", "Short info incorrect"
