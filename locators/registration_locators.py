from selenium.webdriver.common.by import By


class RegistrationLocators:
    EMAIL_INPUT = (By.NAME, "email")
    USERNAME_INPUT = (By.NAME, "username")
    FIRST_NAME_INPUT = (By.NAME, "first_name")
    LAST_NAME_INPUT = (By.NAME, "last_name")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")


