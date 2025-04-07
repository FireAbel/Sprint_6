import allure
from pages.main_page import MainPage
from urls import Url


@allure.feature('Перенаправление при нажатии на логотипы')
class TestRedirects:
    @allure.title('Перенаправление при нажатии на логотип "Самокат"')
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)

        main_page.open(Url.ORDER)
        main_page.close_cookie_window()
        main_page.click_scooter_logo()

        assert Url.BASE in main_page.get_current_url()

    @allure.title('Перенаправление при нажатии на логотип "Яндекс"')
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)

        main_page.open(Url.BASE)
        main_page.close_cookie_window()
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        main_page.wait_for_page_load()
        assert Url.DZEN in main_page.get_current_url()
