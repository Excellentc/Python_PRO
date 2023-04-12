from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

page_url = 'https://demoqa.com/elements'


class ElementsPage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.element_categories = By.XPATH, '//div[contains(@class, "show")]//li'

    def open(self):
        self.driver.get(page_url)
        return self

    def get_elements_page_categories(self):
        categories = [cat.text for cat in self.driver.find_elements(*self.element_categories)]
        return categories
