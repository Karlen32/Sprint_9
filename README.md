# Sprint_9 — автотесты для «Продуктовый помощник»

Автотесты на Selenium + pytest + Allure для сервиса «Продуктовый помощник».

## Структура проекта

```Sprint_9/
├── assets/                 # изображения для тестов (например, logo.jpg)
├── pages/                  # Page Object (без локаторов)
│   ├── base_page.py
│   ├── main_page.py
│   ├── login_page.py
│   ├── registration_page.py
│   └── recipe_page.py
├── locators/
│   ├── main_locators.py
│   ├── login_locators.py
│   ├── registration_locators.py
│   └── recipe_locators.py
├── data/
│   └── test_data.py
├── tests/
│   ├── test_registration.py
│   ├── test_login.py
│   └── test_recipe.py
├── config.py               # BASE_URL, ASSETS_DIR, таймауты
├── conftest.py             # фикстуры (driver, base_url, authorized_user, receipt_payload)
├── pytest.ini
├── requirements.txt
├── browsers.json           # конфигурация браузеров для Selenoid
├── Dockerfile
├── docker-compose.yml
├── .github/workflows/ci.yml
└── README.md
```

## Подготовка

1. Установите Chrome.
2. Клонируйте репозиторий и перейдите в каталог проекта.
3. Создайте виртуальное окружение и установите зависимости:

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

4. При необходимости укажите URL приложения (по умолчанию используется `https://foodgram-frontend-1.prakticum-team.ru`):

```bash
export BASE_URL=https://ваш-сервис.example.com
```

## Запуск тестов локально

```bash
pytest
```

# Sprint_9
# Sprint_9
