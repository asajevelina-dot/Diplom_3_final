import allure
from pages.main_page import MainPage
from data.urls import BASE_URL


@allure.suite("Конструктор бургера")
class TestConstructor:

    @allure.title("Переход по клику на Конструктор")
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor()
        assert main_page.get_current_url() == BASE_URL

    @allure.title("Переход по клику на Лента заказов")
    def test_click_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        assert "feed" in main_page.get_current_url()

    @allure.title("Всплывающее окно открывается при клике на ингредиент")
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
        main_page.wait_modal_invisible()
        assert not main_page.is_modal_visible()

    @allure.title("При добавлении ингредиента счётчик увеличивается")
    def test_counter_increases(self, driver):
        main_page = MainPage(driver)
        counter_before = main_page.get_counter_value()
        main_page.add_filling_to_order()
        main_page.wait_counter_increases(counter_before)  # ✅ Используем метод page object
        counter_after = main_page.get_counter_value()
        assert counter_after > counter_before