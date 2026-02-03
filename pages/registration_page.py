import allure
from pages.base_page import BasePage
from locators.registration_locators import RegistrationLocators


class RegistrationPage(BasePage):
    @allure.step("Заполнить форму регистрации")
    def fill_registration_form(
        self, email, username, first_name, last_name, password
    ):
        self.wait_for_element_visible(
            RegistrationLocators.EMAIL_INPUT
        ).send_keys(email)
        self.wait_for_element_visible(
            RegistrationLocators.USERNAME_INPUT
        ).send_keys(username)
        self.wait_for_element_visible(
            RegistrationLocators.FIRST_NAME_INPUT
        ).send_keys(first_name)
        self.wait_for_element_visible(
            RegistrationLocators.LAST_NAME_INPUT
        ).send_keys(last_name)
        self.wait_for_element_visible(
            RegistrationLocators.PASSWORD_INPUT
        ).send_keys(password)

    @allure.step("Отправить форму регистрации")
    def submit_registration(self):
        self.wait_for_element_clickable(
            RegistrationLocators.SUBMIT_BUTTON
        ).click()