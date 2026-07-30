from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC


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