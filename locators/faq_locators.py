class FaqLocators:
    QUESTION_LOCATOR = "//div[contains(text(), '{}')]"
    ANSWER_LOCATOR = "//div[contains(text(), '{}')]/../..//div[@class='accordion__panel']/p"
    FAQ_SECTION =  "//div[@class='Home_FAQ__3uVm4']"