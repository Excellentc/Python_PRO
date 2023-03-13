class TestMobileDevicesPositive:

    def test_mobile_brand_type(self, mobile_device_positive):
        assert type(mobile_device_positive.brand) == str, 'Type result is incorrect'

    def test_mobile_model_type(self, mobile_device_positive):
        assert type(mobile_device_positive.model) == str, 'Type result is incorrect'

    def test_mobile_price_type(self, mobile_device_positive):
        assert type(mobile_device_positive.price) == float, 'Type result is incorrect'

    def test_mobile_os_type(self, mobile_device_positive):
        assert type(mobile_device_positive.os) == str, 'Type result is incorrect'

    def test_mobile_brand(self, mobile_device_positive):
        assert mobile_device_positive.brand == "Apple", 'Value result is incorrect'

    def test_mobile_model(self, mobile_device_positive):
        assert mobile_device_positive.model == "iPhone 6", 'Value result is incorrect'

    def test_mobile_price(self, mobile_device_positive):
        assert mobile_device_positive.price == 250.5, 'Value result is incorrect'

    def test_mobile_os(self, mobile_device_positive):
        assert mobile_device_positive.os == "iOS", 'Value result is incorrect'

    def test_mobile_get_short_info(self, mobile_device_positive):
        assert mobile_device_positive.get_short_info() == "Apple iPhone 6, 250.5$, OS: iOS", "Short info incorrect"


class TestMobileDevicesNegative:

    def test_mobile_brand_type(self, mobile_device_negative):
        assert type(mobile_device_negative.brand) != str, 'Type result is incorrect'

    def test_mobile_model_type(self, mobile_device_negative):
        assert type(mobile_device_negative.model) != str, 'Type result is incorrect'

    def test_mobile_price_type(self, mobile_device_negative):
        assert type(mobile_device_negative.price) == int, 'Type result is incorrect'

    def test_mobile_os_type(self, mobile_device_negative):
        assert type(mobile_device_negative.os) != str, 'Type result is incorrect'

    def test_mobile_brand(self, mobile_device_negative):
        assert mobile_device_negative.brand != "Apple", 'Value result is incorrect'

    def test_mobile_model(self, mobile_device_negative):
        assert mobile_device_negative.model != "iPhone 6", 'Value result is incorrect'

    def test_mobile_price(self, mobile_device_negative):
        assert mobile_device_negative.price == 250, 'Value result is incorrect'

    def test_mobile_os(self, mobile_device_negative):
        assert mobile_device_negative.os != "iOS", 'Value result is incorrect'
