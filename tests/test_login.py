import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data.test_data import LOGIN_USER


class TestLogin:
    @allure.title("Авторизация пользователя")
    def test_login_redirects_to_main_and_logout_button_visible(
        self, driver, base_url
    ):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver, base_url)
            main_page.open()

        with allure.step("Нажать кнопку «Войти»"):
            main_page.click_login()

        with allure.step("Выполнить авторизацию пользователя"):
            login_page = LoginPage(driver, base_url)
            login_page.login(
                email=LOGIN_USER["email"],
                password=LOGIN_USER["password"],
            )

        with allure.step("Проверить отображение кнопки «Выход»"):
            assert main_page.is_logout_button_visible()

