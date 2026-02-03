from faker import Faker

faker = Faker("ru_RU")


def generate_registration_user():
    return {
        "email": faker.unique.email(),
        "username": faker.unique.user_name(),
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "password": faker.password(
            length=12,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ),
    }


LOGIN_USER = {
    "email": "asa",
    "password": "lkjhgfdsa123",
}

RECIPE_IMAGE_FILENAME = "logo.jpg"

RECIPE_DATA = {
    "name": "Тестовый рецепт борща",
    "description": "Описание тестового рецепта для автотеста.",
    "cooking_time": 60,
    "ingredient_search": "св",
    "ingredient_name": "Свекла",
    "ingredient_amount": "100",
}