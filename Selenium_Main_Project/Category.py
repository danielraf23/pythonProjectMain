from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Category:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_into_product(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "[class ='cell categoryRight'] > ul > li")

    def click_on_product(self, num):
        self.get_into_product()[num].click()

    def back_to_homepage(self):
        return self.driver.find_element(By.CSS_SELECTOR,'a[translate="HOME"]')