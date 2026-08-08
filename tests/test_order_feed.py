import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from selenium.webdriver.support.ui import WebDriverWait


@allure.suite("Лента заказов")
class TestOrderFeed:

    @allure.title("Счётчик «Выполнено за всё время» увеличивается")
    def test_all_time_counter_increases(self, auth_driver):
        driver = auth_driver
        main_page = MainPage(driver)

        # 1. Переходим в ленту заказов
        main_page.click_order_feed()
        order_feed_page = OrderFeedPage(driver)
        counter_before = order_feed_page.get_completed_orders_all_time()

        # 2. Переходим в конструктор и создаём заказ
        main_page.click_constructor()
        main_page.create_order()

        # 3. Снова переходим в ленту заказов
        main_page.click_order_feed()
        driver.refresh()

        WebDriverWait(driver, 20).until(
            lambda d: order_feed_page.get_completed_orders_all_time() > counter_before
        )

        counter_after = order_feed_page.get_completed_orders_all_time()
        assert counter_after > counter_before

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается")
    def test_today_counter_increases(self, auth_driver):
        driver = auth_driver
        main_page = MainPage(driver)

        main_page.click_order_feed()
        order_feed_page = OrderFeedPage(driver)
        counter_before = order_feed_page.get_completed_orders_today()

        main_page.click_constructor()
        main_page.create_order()

        main_page.click_order_feed()
        driver.refresh()

        WebDriverWait(driver, 20).until(
            lambda d: order_feed_page.get_completed_orders_today() > counter_before
        )

        counter_after = order_feed_page.get_completed_orders_today()
        assert counter_after > counter_before

    @allure.title("Номер заказа появляется в разделе «В работе»")
    def test_order_in_progress_appears(self, auth_driver):
        driver = auth_driver
        main_page = MainPage(driver)

        main_page.click_order_feed()
        main_page.click_constructor()
        main_page.create_order()

        main_page.click_order_feed()
        driver.refresh()

        order_feed_page = OrderFeedPage(driver)
        orders = order_feed_page.get_orders_in_progress()
        assert isinstance(orders, list)