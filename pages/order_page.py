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

    def fill_first_page(self, name, last_name, address, metro_station, phone):
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(OrderPageLocators.NAME_INPUT)
            ).send_keys(name)

            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(OrderPageLocators.LAST_NAME_INPUT)
            ).send_keys(last_name)

            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(OrderPageLocators.ADDRESS_INPUT)
            ).send_keys(address)

            metro_input = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(OrderPageLocators.METRO_STATION_INPUT)
            )
            metro_input.send_keys(metro_station)

            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(OrderPageLocators.METRO_STATION_OPTION)
            ).click()

            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(OrderPageLocators.PHONE_INPUT)
            ).send_keys(phone)

            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON)
            ).click()


    def fill_second_page(self, date, comment):
        date_input = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(OrderPageLocators.DATE_INPUT))
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.RETURN)

        dropdown = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_DROPDOWN))
        dropdown.click()

        option = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_OPTION))
        option.click()

        color_checkbox = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(OrderPageLocators.COLOR_CHECKBOX))
        self.driver.execute_script("arguments[0].scrollIntoView();", color_checkbox)

        if not color_checkbox.is_selected():
            color_checkbox.click()

        assert color_checkbox.is_selected(), "Цвет не был выбран"

        comment_input = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(OrderPageLocators.COMMENT_INPUT))
        comment_input.send_keys(comment)

        order_button = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", order_button)
        self.driver.execute_script("arguments[0].click();", order_button)

        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_SUCCESS_MODAL))
        confirm_button = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(OrderPageLocators.CONFIRM_ORDER_BUTTON))
        confirm_button.click()

    def check_order_success(self):
        return self.find_element(OrderPageLocators.ORDER_SUCCESS_MODAL).text
