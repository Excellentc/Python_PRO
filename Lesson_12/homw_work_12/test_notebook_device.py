class TestNotebookDevicesPositive:

    def test_mobile_brand_type(self, notebook_device_positive):
        assert type(notebook_device_positive.brand) == str, 'Type result is incorrect'

    def test_mobile_model_type(self, notebook_device_positive):
        assert type(notebook_device_positive.model) == str, 'Type result is incorrect'

    def test_mobile_price_type(self, notebook_device_positive):
        assert type(notebook_device_positive.price) == float or int, 'Type result is incorrect'

    def test_mobile_scr_size_type(self, notebook_device_positive):
        assert type(notebook_device_positive.screen_size) == str, 'Type result is incorrect'

    def test_mobile_brand(self, notebook_device_positive):
        assert notebook_device_positive.brand == "HP", 'Value result is incorrect'

    def test_mobile_model(self, notebook_device_positive):
        assert notebook_device_positive.model == "L34006", 'Value result is incorrect'

    def test_mobile_price(self, notebook_device_positive):
        assert notebook_device_positive.price == 1100, 'Type result is incorrect'

    def test_mobile_scr_size(self, notebook_device_positive):
        assert notebook_device_positive.screen_size == "15.2 inches", 'Value result is incorrect'

    def test_mobile_get_short_info(self, notebook_device_positive):
        assert notebook_device_positive.get_short_info() == "HP L34006, 1100$, Screen Size: 15.2 inches", \
            "Short info incorrect"


class TestNotebookDevicesNegative:

    def test_notebook_brand_type(self, notebook_device_negative):
        assert type(notebook_device_negative.brand) != str, 'Type result is incorrect'

    def test_notebook_model_type(self, notebook_device_negative):
        assert type(notebook_device_negative.model) != str, 'Type result is incorrect'

    def test_notebook_price_type(self, notebook_device_negative):
        assert type(notebook_device_negative.price) != int or float, 'Type result is incorrect'

    def test_notebook_scr_size_type(self, notebook_device_negative):
        assert type(notebook_device_negative.screen_size) != str, 'Type result is incorrect'

    def test_notebook_brand(self, notebook_device_negative):
        assert notebook_device_negative.brand != "HP", 'Value result is incorrect'

    def test_notebook_model(self, notebook_device_negative):
        assert notebook_device_negative.model != "L34006", 'Value result is incorrect'

    def test_notebook_price(self, notebook_device_negative):
        assert notebook_device_negative.price == 1100, 'Value result is incorrect'

    def test_notebook_scr_size(self, notebook_device_negative):
        assert notebook_device_negative.screen_size != "15.2 inches", 'Value result is incorrect'
