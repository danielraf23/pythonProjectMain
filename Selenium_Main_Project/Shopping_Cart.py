from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Shopping_cart:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def shopping_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class="select  ng-binding"]').get_attribute("innerHTML")[1:]

    def checkout(self):
        return self.driver.find_element(By.ID ,"checkOutPopUp")

    def shopping_cart_is_empty(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".bigEmptyCart>label")