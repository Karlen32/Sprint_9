from selenium.webdriver.common.by import By


class MainLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/signin']")
    REGISTER_BUTTON = (By.LINK_TEXT, "Создать аккаунт")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Выход")
    CREATE_RECIPE_TAB = (
        By.XPATH,
        "//a[contains(text(),'Создать рецепт') or contains(@href,'recipes/create')]",
    )