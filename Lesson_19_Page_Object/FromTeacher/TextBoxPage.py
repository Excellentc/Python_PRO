from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TextBoxPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = 'https://demoqa.com/text-box'
        self.full_name_field = (By.ID, 'userName')
        self.email_field = (By.ID, 'userEmail')
        self.current_address_text_area = (By.CSS_SELECTOR, 'textarea#currentAddress')
        self.permanent_address_text_area = (By.CSS_SELECTOR, 'textarea#permanentAddress')
        self.submit_button = (By.ID, 'submit')
        self.result_full_name = (By.ID, 'name')
        self.result_email = (By.ID, 'email')
        self.result_curr_addr = (By.CSS_SELECTOR, 'p#currentAddress')
        self.result_perm_addr = (By.CSS_SELECTOR, 'p#permanentAddress')

    def open(self) -> 'TextBoxPage':
        self.driver.get(self.url)
        return self

    def clear_full_name_field(self) -> None:
        self.driver.find_element(*self.full_name_field).clear()

    def fill_full_name_field(self, text: str) -> None:
        self.driver.find_element(*self.full_name_field).send_keys(text)

    def clear_email_field(self) -> None:
        self.driver.find_element(*self.email_field).clear()

    def fill_email_field(self, text: str) -> None:
        self.driver.find_element(*self.email_field).send_keys(text)

    def clear_current_address_field(self) -> None:
        self.driver.find_element(*self.current_address_text_area).clear()

    def fill_current_address_field(self, text: str) -> None:
        self.driver.find_element(*self.current_address_text_area).send_keys(
            text)

    def clear_permanent_address_field(self) -> None:
        self.driver.find_element(*self.permanent_address_text_area).clear()

    def fill_permanent_address_field(self, text: str) -> None:
        self.driver.find_element(*self.permanent_address_text_area).send_keys(
            text)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def get_result_fullname(self):
        return self.driver.find_element(*self.result_full_name).text

    def get_result_email(self):
        return self.driver.find_element(*self.email_field).text

    def get_result_curr_addr(self):
        return self.driver.find_element(*self.result_curr_addr).text

    def get_result_perm_addr(self):
        return self.driver.find_element(*self.result_perm_addr).text
