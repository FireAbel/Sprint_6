from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.base_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    def find_element(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def close_cookie_window(self):
        self.find_element(BasePageLocators.COOKIE_BUTTON).click()

    def switch_to_new_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])
