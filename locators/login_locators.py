from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
