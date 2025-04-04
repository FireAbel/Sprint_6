import allure
from selenium.webdriver.remote.webdriver import WebDriver
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Кликаем по кнопке 'Заказать' в хедере")
    def click_order_button_header(self):
        self.click(self.locators.HEADER_ORDER)

    @allure.step("Кликаем по кнопке 'Заказать' в футере")
    def click_order_button_footer(self):
        self.scroll_to_locator(self.locators.FOOTER_ORDER)
        self.click(self.locators.FOOTER_ORDER)

    @allure.step("Кликаем по логотипу 'Самокат'")
    def click_scooter_logo(self):
        self.click(self.locators.SCOOTER_LOGO)

    @allure.step("Кликаем по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        self.click(self.locators.YANDEX_LOGO)

    @allure.step("Закрываем окно cookies")
    def close_cookie_window(self):
        self.click(self.locators.COOKIE_BUTTON)
