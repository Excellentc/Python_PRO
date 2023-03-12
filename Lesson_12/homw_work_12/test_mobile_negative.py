def test_mobile_brand_type(mobile_device_negative):
    assert type(mobile_device_negative.brand) != str, 'Type result is incorrect'


def test_mobile_model_type(mobile_device_negative):
    assert type(mobile_device_negative.model) != str, 'Type result is incorrect'


def test_mobile_price_type(mobile_device_negative):
    assert type(mobile_device_negative.price) == int, 'Type result is incorrect'


def test_mobile_os_type(mobile_device_negative):
    assert type(mobile_device_negative.os) != str, 'Type result is incorrect'


def test_mobile_brand(mobile_device_negative):
    assert mobile_device_negative.brand != "Apple", 'Value result is incorrect'


def test_mobile_model(mobile_device_negative):
    assert mobile_device_negative.model != "iPhone 6", 'Value result is incorrect'


def test_mobile_price(mobile_device_negative):
    assert mobile_device_negative.price == 250, 'Value result is incorrect'


def test_mobile_os(mobile_device_negative):
    assert mobile_device_negative.os != "iOS", 'Value result is incorrect'
