from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.faq_locators import FaqLocators
from pages.base_page import BasePage


class FaqPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_question_locator(self, question_text):
        return (By.XPATH, FaqLocators.QUESTION_LOCATOR.format(question_text))

    def get_answer_locator(self, question_text):
        return (By.XPATH, FaqLocators.ANSWER_LOCATOR.format(question_text))

    def click_question(self, question_text):
        question = self.find_element(self.get_question_locator(question_text))
        self.scroll_to_element(question)
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.get_question_locator(question_text)))
        question.click()

    def get_answer_text(self, question_text):
        answer_locator = self.get_answer_locator(question_text)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(answer_locator))
        return self.find_element(answer_locator).text

    def scroll_to_faq_section(self):
        faq_section = self.find_element(FaqLocators.FAQ_SECTION)
        self.scroll_to_element(faq_section)