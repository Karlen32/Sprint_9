import allure
from pathlib import Path

from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from locators.recipe_locators import RecipeLocators


class RecipePage(BasePage):

    @allure.step("Создать рецепт через форму")
    def create_recipe(
        self,
        name,
        ingredient_value,
        ingredient_amount,
        cooking_time,
        description,
        img,
    ):
        if isinstance(img, Path):
            img = str(img.resolve())

        self.wait_for_element_clickable(
            RecipeLocators.CREATE_RECIPE_LINK
        ).click()

        self.wait_for_element_visible(
            RecipeLocators.NAME_INPUT
        ).send_keys(name)

        ingredient_input = self.wait_for_element_visible(
            RecipeLocators.INGREDIENT_INPUT
        )
        ingredient_input.send_keys(ingredient_value)

        self.wait_for_element_present(
            RecipeLocators.INGREDIENTS_LIST
        )
        self.click_by_index(
            RecipeLocators.INGREDIENTS_LIST, 0
        )

        amount_input = self.wait_for_element_visible(
            RecipeLocators.INGREDIENT_OPTION
        )
        amount_input.send_keys(str(ingredient_amount))

        self.wait_for_element_clickable(
            RecipeLocators.ADD_INGREDIENT_BUTTON
        ).click()

        self.wait_for_element_visible(
            RecipeLocators.COOKING_TIME_INPUT
        ).send_keys(str(cooking_time))

        self.wait_for_element_visible(
            RecipeLocators.DESCRIPTION_INPUT
        ).send_keys(description)

        file_input = None
        for loc in (RecipeLocators.IMAGE_INPUT, RecipeLocators.IMAGE_INPUT_FALLBACK):
            try:
                file_input = self.wait_for_element_present(loc, timeout=6)
                file_input.send_keys(img)
                break
            except Exception:
                continue
        if file_input is None:
            raise AssertionError("Не найден input для загрузки изображения")

        for btn_loc in (
            RecipeLocators.CREATE_RECIPE_BUTTON_FORM,
            RecipeLocators.CREATE_RECIPE_BUTTON_FALLBACK,
        ):
            try:
                self.scroll_to_element(btn_loc, timeout=10)
                self.wait_for_element_clickable(btn_loc, timeout=8).click()
                break
            except Exception:
                try:
                    self.click_via_js(btn_loc, timeout=5)
                    break
                except Exception:
                    continue
        else:
            raise AssertionError("Кнопка «Создать рецепт» не найдена")

        def success(driver):
            url = driver.current_url
            if "/recipes/" in url and "/recipes/create" not in url:
                return True
            try:
                if driver.find_elements(*RecipeLocators.RECIPE_CARD):
                    return True
            except Exception:
                pass
            return False

        WebDriverWait(self.driver, 25).until(success)

        try:
            return self.wait_for_element_present(RecipeLocators.RECIPE_CARD, timeout=12)
        except Exception:
            return self.wait_for_element_present(RecipeLocators.RECIPE_TITLE_H1, timeout=8)

    @allure.step("Проверить название рецепта в карточке")
    def check_name_in_card(self, expected_name):
        expected = expected_name.strip()
        try:
            actual = self.get_text_by_locator(RecipeLocators.RECIPE_NAME_IN_CARD).strip()
            if expected == actual:
                return True
        except Exception:
            pass
        for el in self.driver.find_elements(*RecipeLocators.RECIPE_TITLE_H1):
            if expected in el.text or el.text.strip() == expected:
                return True
        if "/recipes/" in self.driver.current_url:
            if expected in self.driver.find_element("tag name", "body").text:
                return True
        return False