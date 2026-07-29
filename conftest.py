import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=["chrome"])
def driver(request):
    browser = request.param
    
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
    
    driver.get("https://stellarburgers.education-services.ru/")
    yield driver
    driver.quit()