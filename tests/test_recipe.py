import allure
import pytest

from config import ASSETS_DIR
from data.test_data import RECIPE_IMAGE_FILENAME
from pages.recipe_page import RecipePage


@pytest.mark.usefixtures("driver", "base_url")
class TestCreateRecipe:

    @allure.title("Создание нового рецепта")
    @allure.description("Карточка рецепта и корректное название отображаются после создания")
    def test_create_recipe_success(
        self, driver, base_url, authorized_user, receipt_payload
    ):

        with allure.step("Инициализация страницы создания рецепта"):
            recipe_page = RecipePage(driver, base_url)

        with allure.step("Подготовка изображения рецепта"):
            image_path = str(
                (ASSETS_DIR / RECIPE_IMAGE_FILENAME).resolve()
            )

        with allure.step("Создание рецепта через форму"):
            recipe_card = recipe_page.create_recipe(
                name=receipt_payload["name"],
                ingredient_value="ф",
                ingredient_amount=receipt_payload["ingredient_amount"],
                cooking_time=receipt_payload["cooking_time"],
                description=receipt_payload["description"],
                img=image_path,
            )

        with allure.step("Проверка, что карточка рецепта отображается"):
            assert recipe_card, "Карточка рецепта не отображается"

        with allure.step("Проверка названия рецепта в карточке"):
            assert recipe_page.check_name_in_card(
                receipt_payload["name"]
            )
