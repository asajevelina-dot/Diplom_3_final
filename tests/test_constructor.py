import allure
from pages.main_page import MainPage


@allure.suite("Конструктор бургера")
class TestConstructor:

    @allure.title("Переход по клику на Конструктор")
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor()
        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    @allure.title("Переход по клику на Лента заказов")
    def test_click_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        assert "feed" in driver.current_url

    @allure.title("Клик на ингредиент - появляется всплывающее окно")
    def test_ingredient_modal_appears(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.is_modal_visible()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_ingredient_modal_closes(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.is_modal_visible()
        main_page.close_modal()
        import time
        time.sleep(1)
        assert not main_page.is_modal_visible()