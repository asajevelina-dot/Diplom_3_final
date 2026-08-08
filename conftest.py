import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import allure
from pages.main_page import MainPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")


@pytest.fixture(params=["chrome"])  # ← ТОЛЬКО CHROME (Firefox отключён)
def driver(request):
    browser = request.param
    
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    driver.get("https://stellarburgers.education-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture
def auth_driver(driver):
    """Фикстура для авторизованного драйвера"""
    main_page = MainPage(driver)
    EMAIL = "anna.maria@yandex.ru"
    PASSWORD = "MySecretPassword123"
    main_page.login(EMAIL, PASSWORD)
    return driver