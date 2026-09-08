from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators, AuthLoginLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import re


class MainPage(BasePage):
    
    # ====== НАВИГАЦИЯ ======
    
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDERS_LIST_BUTTON)
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.ORDERS_LIST_TITLE))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)

    def click_profile(self):
        self.click_element(MainPageLocators.PROFILE_BUTTON)

    # ====== ИНГРЕДИЕНТЫ ======
    
    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT)

    def is_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    def close_modal(self):
        self.click_element(MainPageLocators.CROSS_BUTTON)

    def wait_modal_invisible(self):
        self.wait.until(EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS_POPUP))

    # ====== ПЕРЕТАСКИВАНИЕ ======
    
    def drag_and_drop_on_element(self, draggable_locator, droppable_locator):
        draggable = self.wait.until(EC.presence_of_element_located(draggable_locator))
        droppable = self.wait.until(EC.presence_of_element_located(droppable_locator))
        actions = ActionChains(self.driver)
        actions.drag_and_drop(draggable, droppable).perform()
        time.sleep(0.5)

    def add_filling_to_order(self):
        self.drag_and_drop_on_element(
            MainPageLocators.BUN_INGREDIENT,
            MainPageLocators.ORDER_BASKET
        )

    def add_ingredient_to_order(self):
        self.drag_and_drop_on_element(
            MainPageLocators.SAUCE_INGREDIENT,
            MainPageLocators.ORDER_BASKET
        )

    # ====== СЧЕТЧИК ======
    
    def get_counter_value(self):
        """Возвращает значение счётчика для булки"""
        try:
            counter = self.wait.until(
                EC.visibility_of_element_located(MainPageLocators.COUNTER)  # ✅ Используем локатор
            )
            text = counter.text.strip()
            try:
                return int(text)
            except ValueError:
                m = re.search(r'\d+', text)
                return int(m.group()) if m else 0
        except Exception:
            return 0

    def wait_counter_increases(self, initial_value):
        """Ожидает увеличения счетчика"""
        self.wait.until(
            lambda d: self.get_counter_value() > initial_value
        )

    # ====== АВТОРИЗАЦИЯ ======
    
    def login(self, email, password):
        login_button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_PROFILE_BUTTON))
        login_button.click()

        email_input = self.wait.until(EC.visibility_of_element_located(AuthLoginLocators.EMAIL_FIELD))
        email_input.send_keys(email)

        password_input = self.wait.until(EC.visibility_of_element_located(AuthLoginLocators.PASSWORD_FIELD))
        password_input.send_keys(password)

        submit_button = self.wait.until(EC.element_to_be_clickable(AuthLoginLocators.LOGIN_BUTTON_ANY_FORMS))
        submit_button.click()

        self.wait.until(EC.visibility_of_element_located(MainPageLocators.PROFILE_BUTTON))

    # ====== ЗАКАЗЫ ======
    
    def wait_order_id(self):
        """Ожидает появления номера заказа"""
        order_id_element = self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_ID)
        )
        self.wait.until(
            lambda d: order_id_element.text != "9999"
        )
        return order_id_element.text

    def close_order_modal(self):
        """Закрывает модальное окно заказа"""
        close_button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.CLOSE_MODAL_ORDER))
        close_button.click()
        time.sleep(1)

    def create_order(self):
        """Создаёт заказ (перетаскиваем булку и соус)"""
        self.add_filling_to_order()
        self.add_ingredient_to_order()
        
        order_button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.CREATE_ORDER_BUTTON))
        order_button.click()
        
        order_id = self.wait_order_id()
        self.close_order_modal()
        return order_id

    def refresh_and_wait_orders(self):
        """Обновляет страницу и ждет загрузки заказов"""
        self.driver.refresh()
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.ORDERS_LIST_TITLE))
        time.sleep(1)