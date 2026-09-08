from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.support import expected_conditions as EC
import re


class OrderFeedPage(BasePage):
    
    def _to_int(self, text):
        """Безопасное преобразование текста в число"""
        try:
            return int(text.strip())
        except ValueError:
            m = re.search(r'\d+', text)
            return int(m.group()) if m else 0

    def get_completed_orders_all_time(self):
        """Возвращает значение счётчика «Выполнено за всё время»"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = self.wait.until(EC.visibility_of_element_located(OrderFeedLocators.COMPLETED_ORDERS_ALL_TIME))
        return self._to_int(element.text)

    def get_completed_orders_today(self):
        """Возвращает значение счётчика «Выполнено за сегодня»"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = self.wait.until(EC.visibility_of_element_located(OrderFeedLocators.COMPLETED_ORDERS_TODAY))
        return self._to_int(element.text)

    def get_orders_in_progress(self):
        """Возвращает список заказов в разделе «В работе»"""
        self.wait.until(EC.presence_of_all_elements_located(OrderFeedLocators.ORDERS_IN_PROGRESS))
        elements = self.driver.find_elements(*OrderFeedLocators.ORDERS_IN_PROGRESS)
        return [el.text for el in elements]

    def wait_counter_increases_all_time(self, initial_value):
        """Ожидает увеличения счётчика «Выполнено за всё время»"""
        self.wait.until(
            lambda d: self.get_completed_orders_all_time() > initial_value
        )

    def wait_counter_increases_today(self, initial_value):
        """Ожидает увеличения счётчика «Выполнено за сегодня»"""
        self.wait.until(
            lambda d: self.get_completed_orders_today() > initial_value
        )