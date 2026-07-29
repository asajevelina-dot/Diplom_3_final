from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MainPage(BasePage):
    # Локаторы через href (самые надёжные)
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@href='/']")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[@href='/feed']")
    
    INGREDIENT = (By.XPATH, "//*[contains(@class, 'BurgerIngredient_ingredient__')]")
    INGREDIENT_DETAILS = (By.XPATH, "//*[contains(@class, 'Modal_modal__')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__')]")

    def click_constructor(self):
        self.click_element(self.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.click_element(self.ORDER_FEED_BUTTON)

    def click_ingredient(self):
        # Ждём, пока ингредиенты загрузятся
        self.wait.until(EC.presence_of_element_located(self.INGREDIENT))
        self.click_element(self.INGREDIENT)

    def is_modal_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.INGREDIENT_DETAILS))
            return True
        except:
            return False

    def close_modal(self):
        self.click_element(self.CLOSE_BUTTON)