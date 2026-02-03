import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data.test_data import LOGIN_USER, RECIPE_DATA
from config import BASE_URL



@pytest.fixture(scope="function")
def receipt_payload():
    return RECIPE_DATA.copy()


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    use_selenoid = os.getenv("USE_SELENOID", "0") == "1"
    selenoid_uri = os.getenv("SELENOID_URI")

    if use_selenoid and selenoid_uri:
        driver = webdriver.Remote(
            command_executor=selenoid_uri,
            options=options,
        )
    else:
        driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def base_url():
    return BASE_URL.rstrip("/")


@pytest.fixture(scope="function")
def authorized_user(driver, base_url):
    main_page = MainPage(driver, base_url)
    main_page.open()
    main_page.click_login()

    login_page = LoginPage(driver, base_url)
    login_page.login(
        email=LOGIN_USER["email"],
        password=LOGIN_USER["password"],
    )