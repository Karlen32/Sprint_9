from selenium.webdriver.common.by import By


class RecipeLocators:
    CREATE_RECIPE_LINK = (By.CSS_SELECTOR, "a[href='/recipes/create']")

    NAME_INPUT = (
        By.XPATH,
        "//label[.//div[contains(.,'Название рецепта')]]//input"
    )

    INGREDIENT_INPUT = (
        By.XPATH,
        "//label[.//div[contains(.,'Ингредиенты')]]//input"
    )

    INGREDIENTS_LIST = (
        By.CLASS_NAME,
        "styles_container__3ukwm"
    )

    INGREDIENT_OPTION = (
        By.CSS_SELECTOR,
        "input.styles_ingredientsAmountValue__2matT"
    )

    ADD_INGREDIENT_BUTTON = (
        By.XPATH,
        "//div[normalize-space()='Добавить ингредиент']"
    )

    COOKING_TIME_INPUT = (
        By.XPATH,
        "//label[.//div[contains(.,'Время приготовления')]]//input"
    )

    DESCRIPTION_INPUT = (
        By.XPATH,
        "//label[.//div[contains(.,'Описание рецепта')]]//textarea"
    )

    IMAGE_INPUT = (
        By.XPATH,
        "//form[.//button[contains(., 'Создать рецепт')]]//input[@type='file']"
    )
    IMAGE_INPUT_FALLBACK = (By.CSS_SELECTOR, "input[type='file']")
    
    CREATE_RECIPE_BUTTON_FORM = (
        By.XPATH,
        "//button[contains(@class, 'style_button') and contains(., 'Создать рецепт')]"
    )
    CREATE_RECIPE_BUTTON_FALLBACK = (
        By.XPATH,
        "//button[contains(., 'Создать рецепт')]"
    )

    RECIPE_CARD = (
        By.CLASS_NAME,
        "styles_single-card__1yTTj"
    )

    RECIPE_NAME_IN_CARD = (
        By.CSS_SELECTOR,
        ".styles_single-card__header-info__3B9iz h1"
    )
    RECIPE_TITLE_H1 = (By.TAG_NAME, "h1")