import allure

from pages.base_page import BasePage
from locators.recipe_locators import CreateRecipeLocators


class CreateRecipePage(BasePage):

    @allure.step("Заполнить форму создания рецепта")
    def fill_recipe_form(
        self, name, description, cooking_time, image_path=None, ingredient_search=None
    ):
        self.wait_for_element_visible(CreateRecipeLocators.NAME_INPUT).send_keys(name)
        self.wait_for_element_visible(CreateRecipeLocators.DESCRIPTION_INPUT).send_keys(description)
        self.wait_for_element_visible(CreateRecipeLocators.COOKING_TIME_INPUT).send_keys(
            str(cooking_time)
        )
        if image_path:
            self.wait_for_element_visible(CreateRecipeLocators.IMAGE_INPUT).send_keys(image_path)
        if ingredient_search:
            ingredient_field = self.wait_for_element_visible(CreateRecipeLocators.INGREDIENT_INPUT)
            ingredient_field.send_keys(ingredient_search)
            option = self.wait_for_element_clickable(CreateRecipeLocators.INGREDIENT_OPTION)
            option.click()

    @allure.step("Нажать кнопку «Создать рецепт»")
    def submit_recipe(self):
        element = self.wait_for_element_clickable(CreateRecipeLocators.SUBMIT_BUTTON)
        element.click()

    @allure.step("Проверить отображение карточки рецепта с названием")
    def is_recipe_card_with_title_visible(self, expected_title):
        if not self.is_element_present(CreateRecipeLocators.RECIPE_CARD_TITLE):
            return False
        elements = self.driver.find_elements(*CreateRecipeLocators.RECIPE_CARD_TITLE)
        for el in elements:
            if expected_title in el.text:
                return True
        return False
