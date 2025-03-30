import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import OrderData


@allure.feature('Проверка заказа')
class TestOrder:
    @allure.title('Проверка заказа через кнопку {order_button} с данными: {order_data}')
    @pytest.mark.parametrize('order_button, order_data', [
        ('header', OrderData.FIRST_ORDER),
        ('footer', OrderData.SECOND_ORDER)
    ])
    def test_order_flow(self, driver, order_button, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step('Открытие главной страницы'):
            main_page.driver.get('https://qa-scooter.praktikum-services.ru/')
            main_page.close_cookie_window()

        with allure.step(f'Нажатие на кнопку заказа {order_button}'):
            if order_button == 'header':
                main_page.click_order_button_header()
            else:
                main_page.click_order_button_footer()

        with allure.step('Заполнение первой части формы заказа'):
            order_page.fill_first_page(
                order_data['name'],
                order_data['last_name'],
                order_data['address'],
                order_data['metro_station'],
                order_data['phone']
            )

        with allure.step('Заполнение второй части формы заказа'):
            order_page.fill_second_page(
                order_data['date'],
                order_data['comment']
            )

        with allure.step('Проверка успешного заказа'):
            assert "Заказ оформлен" in order_page.check_order_success()
