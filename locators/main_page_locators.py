from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER_ORDER = (By.XPATH, "(//button[text()='Заказать'])[1]")
    FOOTER_ORDER = (By.XPATH, "(//button[text()='Заказать'])[2]")
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')