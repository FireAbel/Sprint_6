import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import OrderData, OrderMessages
from urls import Url


@allure.feature('Проверка заказа')
class TestOrder:
    @allure.title('Проверка заказа через кнопку в хедере')
    def test_order_from_header(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open(Url.BASE)
        main_page.close_cookie_window()
        main_page.click_order_button_header()

        order_page.fill_first_page(
            OrderData.FIRST_ORDER['name'],
            OrderData.FIRST_ORDER['last_name'],
            OrderData.FIRST_ORDER['address'],
            OrderData.FIRST_ORDER['metro_station'],
            OrderData.FIRST_ORDER['phone']
        )

        order_page.fill_second_page(
            OrderData.FIRST_ORDER['date'],
            OrderData.FIRST_ORDER['comment']
        )

        assert OrderMessages.SUCCESS_TEXT in order_page.check_order_success()

    @allure.title('Проверка заказа через кнопку в футере')
    def test_order_from_footer(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open(Url.BASE)
        main_page.close_cookie_window()
        main_page.click_order_button_footer()

        order_page.fill_first_page(
            OrderData.SECOND_ORDER['name'],
            OrderData.SECOND_ORDER['last_name'],
            OrderData.SECOND_ORDER['address'],
            OrderData.SECOND_ORDER['metro_station'],
            OrderData.SECOND_ORDER['phone']
        )

        order_page.fill_second_page(
            OrderData.SECOND_ORDER['date'],
            OrderData.SECOND_ORDER['comment']
        )

        assert OrderMessages.SUCCESS_TEXT in order_page.check_order_success()
