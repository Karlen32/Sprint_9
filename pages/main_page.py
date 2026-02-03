import allure
from pages.base_page import BasePage
from locators.main_locators import MainLocators


class MainPage(BasePage):
    PAGE_PATH = "/"

    @allure.step("Открыть главную страницу")
    def open(self):
        self.open_page(self.PAGE_PATH)

    @allure.step("Нажать кнопку «Войти»")
    def click_login(self):
        self.wait_for_element_clickable(
            MainLocators.LOGIN_BUTTON
        ).click()

    @allure.step("Нажать кнопку «Создать аккаунт»")
    def click_register(self):
        self.wait_for_element_clickable(
            MainLocators.REGISTER_BUTTON
        ).click()

    @allure.step("Нажать таб «Создать рецепт»")
    def click_create_recipe_tab(self):
        self.wait_for_element_clickable(
            MainLocators.CREATE_RECIPE_TAB
        ).click()

    @allure.step("Проверить отображение кнопки «Выход»")
    def is_logout_button_visible(self):
        return self.is_element_present(
            MainLocators.LOGOUT_BUTTON
        )