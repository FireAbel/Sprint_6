import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage


@allure.feature('Перенаправление при нажатии на логотипы')
class TestRedirects:
    @allure.title('Перенаправление при нажатии на логотип "Самокат"')
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)

        with allure.step('Открытие страницы заказа'):
            main_page.driver.get('https://qa-scooter.praktikum-services.ru/order')
            main_page.close_cookie_window()

        with allure.step('Нажатие на логотип "Самокат"'):
            main_page.click_scooter_logo()

        with allure.step('Проверка открытой страницы'):
            assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Перенаправление при нажатии на логотип "Яндекс"')
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)

        with allure.step('Открытие главной страницы'):
            main_page.driver.get('https://qa-scooter.praktikum-services.ru/')
            main_page.close_cookie_window()

        with allure.step('Нажатие на логотип "Яндекс"'):
            main_page.click_yandex_logo()
            main_page.switch_to_new_window()

        with allure.step('Проверка перенаправления на dzen.ru'):
            WebDriverWait(driver, 10).until(EC.url_contains('dzen.ru'))
            assert 'dzen.ru' in driver.current_url