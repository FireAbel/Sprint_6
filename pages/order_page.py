import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    @allure.step("Заполняем первую часть формы заказа")
    def fill_first_page(self, name, last_name, address, metro_station, phone):
        self.send_keys(self.locators.NAME_INPUT, name)
        self.send_keys(self.locators.LAST_NAME_INPUT, last_name)
        self.send_keys(self.locators.ADDRESS_INPUT, address)
        self.send_keys(self.locators.METRO_STATION_INPUT, metro_station)
        self.click(self.locators.METRO_STATION_OPTION)
        self.send_keys(self.locators.PHONE_INPUT, phone)
        self.click(self.locators.NEXT_BUTTON)

    @allure.step("Заполняем вторую часть формы заказа")
    def fill_second_page(self, date, comment):
        self.send_keys(self.locators.DATE_INPUT, date + Keys.RETURN)

        self.click(self.locators.RENTAL_PERIOD_DROPDOWN)
        self.click(self.locators.RENTAL_PERIOD_OPTION)

        self.scroll_to_locator(self.locators.COLOR_CHECKBOX)
        self.click(self.locators.COLOR_CHECKBOX)

        self.send_keys(self.locators.COMMENT_INPUT, comment)

        self.scroll_to_locator(self.locators.ORDER_BUTTON)
        self.click(self.locators.ORDER_BUTTON)

        self.find_visible(self.locators.ORDER_SUCCESS_MODAL)
        self.click(self.locators.CONFIRM_ORDER_BUTTON)

    @allure.step("Проверяем, что заказ оформлен")
    def check_order_success(self):
        return self.find_visible(self.locators.ORDER_SUCCESS_MODAL).text
