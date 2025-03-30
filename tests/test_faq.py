import pytest
import allure
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.faq_page import FaqPage
from data import FaqData


@allure.feature('FaQ секция: Вопросы о важном')
class TestFaq:
    @allure.title('Проверка ответа на вопрос: {question}')
    @pytest.mark.parametrize('question, expected_answer', FaqData.QUESTIONS_ANSWERS.items())
    def test_faq_questions(self, driver, question, expected_answer):
        main_page = MainPage(driver)
        faq_page = FaqPage(driver)

        with allure.step('Открытие главной страницы'):
            main_page.driver.get('https://qa-scooter.praktikum-services.ru/')
            main_page.close_cookie_window()

        with allure.step('Скролл до секции FaQ'):
            faq_section = faq_page.find_element((By.XPATH, "//div[@class='Home_FAQ__3uVm4']"))
            faq_page.scroll_to_element(faq_section)

        with allure.step(f'Нажатие на вопрос: {question}'):
            faq_page.click_question(question)

        with allure.step('Проверка текста ответа'):
            answer = faq_page.get_answer_text(question)
            assert answer == expected_answer, f"Expected answer: {expected_answer}, but got: {answer}"
