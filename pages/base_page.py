from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.find_clickable(locator).click()

    def send_keys(self, locator, value):
        self.find_visible(locator).send_keys(value)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_locator(self, locator):
        element = self.find_element(locator)
        self.scroll_to_element(element)

    def switch_to_new_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 60).until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    def get_current_url(self):
        return self.driver.current_url