from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@href='/']")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[@href='/feed']")
    INGREDIENT = (By.XPATH, "//*[contains(@class, 'BurgerIngredient_ingredient__')]")
    INGREDIENT_DETAILS = (By.XPATH, "//*[contains(@class, 'Modal_modal__')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__')]")
    COUNTER = (By.XPATH, ".//*[contains(@class, 'counter_counter__')]")