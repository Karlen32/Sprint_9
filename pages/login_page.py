import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    @allure.step("Заполнить форму авторизации")
    def fill_login_form(self, email, password):
        self.wait_for_element_visible(
            LoginLocators.EMAIL_INPUT
        ).send_keys(email)

        self.wait_for_element_visible(
            LoginLocators.PASSWORD_INPUT
        ).send_keys(password)

    @allure.step("Нажать кнопку «Войти»")
    def submit_login(self):
        self.wait_for_element_clickable(
            LoginLocators.SUBMIT_BUTTON
        ).click()

    @allure.step("Авторизоваться пользователем")
    def login(self, email, password):
        self.fill_login_form(email, password)
        self.submit_login()

    @allure.step("Проверить отображение формы авторизации")
    def is_login_form_visible(self):
        return (
            self.is_element_present(LoginLocators.EMAIL_INPUT)
            and self.is_element_present(LoginLocators.PASSWORD_INPUT)
        )