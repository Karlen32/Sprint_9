import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url.rstrip("/")

    @allure.step("Открыть страницу {path}")
    def open_page(self, path: str):
        self.driver.get(self.base_url + path)

    @allure.step("Ожидание видимости элемента")
    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание кликабельности элемента")
    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Ожидание наличия элемента в DOM")
    def wait_for_element_present(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Проверка наличия элемента")
    def is_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    @allure.step("Поиск элементов")
    def find_elements(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return self.driver.find_elements(*locator)

    @allure.step("Клик по элементу с индексом {index}")
    def click_by_index(self, locator, index, timeout=10):
        elements = self.find_elements(locator, timeout)
        elements[index].click()

    @allure.step("Получить текст элемента")
    def get_text_by_locator(self, locator, timeout=10):
        element = self.wait_for_element_visible(locator, timeout)
        return element.text

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element_present(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    @allure.step("Ожидание доступности элемента для клика")
    def wait_for_element_enabled(self, locator, timeout=10):
        def _enabled(driver):
            el = driver.find_element(*locator)
            disabled = el.get_attribute("disabled")
            return el if disabled is None or disabled == "false" else False

        WebDriverWait(self.driver, timeout).until(_enabled)

    @allure.step("Клик по элементу через JavaScript")
    def click_via_js(self, locator, timeout=10):
        element = self.wait_for_element_present(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)