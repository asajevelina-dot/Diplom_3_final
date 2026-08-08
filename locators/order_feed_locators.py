from selenium.webdriver.common.by import By


class OrderFeedLocators:
    COMPLETED_ORDERS_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    COMPLETED_ORDERS_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__')]//li[contains(@class, 'text_type_digits-default')]")