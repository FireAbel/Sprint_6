from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.CLASS_NAME, 'select-search__input')
    METRO_STATION_OPTION = (By.CLASS_NAME, 'select-search__row')
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and contains(text(), 'сутки')]")
    BLACK_COLOR = (By.ID, 'black')
    GREY_COLOR = (By.ID, 'grey')
    COLOR_CHECKBOX = BLACK_COLOR
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
