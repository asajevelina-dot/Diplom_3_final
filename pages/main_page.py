from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT)

    def is_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS)

    def close_modal(self):
        self.click_element(MainPageLocators.CLOSE_BUTTON)

    def wait_modal_invisible(self):
        self.wait.until(EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS))

    def add_ingredient_to_order(self):
        """Добавляет ингредиент в заказ (перетаскивание)"""
        ingredient = self.wait.until(EC.element_to_be_clickable(MainPageLocators.INGREDIENT))
        # Находим цель (корзину)
        target = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'BurgerConstructor_basket__')]")))
        # Перетаскиваем ингредиент в корзину
        ActionChains(self.driver).drag_and_drop(ingredient, target).perform()

    def get_counter_value(self):
        """Возвращает значение счётчика ингредиента"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(MainPageLocators.COUNTER))
            return int(element.text) if element.text else 0
        except:
            return 0