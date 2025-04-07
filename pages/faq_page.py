import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from locators.faq_locators import FaqLocators
from pages.base_page import BasePage


class FaqPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = FaqLocators()

    @allure.step("Получаем локатор вопроса: {question_text}")
    def get_question_locator(self, question_text):
        return (By.XPATH, self.locators.QUESTION_LOCATOR.format(question_text))

    @allure.step("Получаем локатор ответа на вопрос: {question_text}")
    def get_answer_locator(self, question_text):
        return (By.XPATH, self.locators.ANSWER_LOCATOR.format(question_text))

    @allure.step("Нажимаем на вопрос: {question_text}")
    def click_question(self, question_text):
        locator = self.get_question_locator(question_text)
        self.scroll_to_locator(locator)
        self.click(locator)

    @allure.step("Получаем текст ответа на вопрос: {question_text}")
    def get_answer_text(self, question_text):
        locator = self.get_answer_locator(question_text)
        return self.find_visible(locator).text

    @allure.step("Скроллим до секции FAQ")
    def scroll_to_faq_section(self):
        self.scroll_to_locator((By.XPATH, self.locators.FAQ_SECTION))
