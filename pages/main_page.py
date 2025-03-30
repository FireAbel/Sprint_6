from selenium.webdriver.remote.webdriver import WebDriver
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    def click_order_button_header(self):
        self.find_element(self.locators.HEADER_ORDER).click()

    def click_order_button_footer(self):
        footer_button = self.find_element(self.locators.FOOTER_ORDER)
        self.scroll_to_element(footer_button)
        footer_button.click()

    def click_scooter_logo(self):
        self.find_element(self.locators.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        self.find_element(self.locators.YANDEX_LOGO).click()

