import allure
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.main_page import MainPage
from data.test_data import generate_registration_user


class TestRegistration:
    @allure.title("Регистрация пользователя")
    def test_registration_redirects_to_login_and_form_visible(
        self, driver, base_url
    ):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver, base_url)
            main_page.open()

        with allure.step("Нажать кнопку «Создать аккаунт»"):
            main_page.click_register()

        with allure.step("Сгенерировать тестовые данные пользователя"):
            user = generate_registration_user()

        with allure.step("Заполнить форму регистрации"):
            registration_page = RegistrationPage(driver, base_url)
            registration_page.fill_registration_form(
                email=user["email"],
                username=user["username"],
                first_name=user["first_name"],
                last_name=user["last_name"],
                password=user["password"],
            )

        with allure.step("Отправить форму регистрации"):
            registration_page.submit_registration()

        with allure.step(
            "Проверить переход на страницу авторизации и отображение формы входа"
        ):
            login_page = LoginPage(driver, base_url)
            assert login_page.is_login_form_visible()

