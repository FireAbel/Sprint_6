import pytest
import allure
from pages.main_page import MainPage
from pages.faq_page import FaqPage
from data import FaqData
from urls import Url


@allure.feature('FaQ секция: Вопросы о важном')
class TestFaq:
    @allure.title('Проверка ответа на вопрос: {question}')
    @pytest.mark.parametrize('question, expected_answer', FaqData.QUESTIONS_ANSWERS.items())
    def test_faq_questions(self, driver, question, expected_answer):
        main_page = MainPage(driver)
        faq_page = FaqPage(driver)

        main_page.open(Url.BASE)
        main_page.close_cookie_window()

        faq_page.scroll_to_faq_section()
        faq_page.click_question(question)

        answer = faq_page.get_answer_text(question)
        assert answer == expected_answer