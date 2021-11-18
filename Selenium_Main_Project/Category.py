from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Category:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def product(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "[class ='cell categoryRight'] > ul > li")

    # get a number and click on the index of it on the products list
    def click_on_product(self, num):
        self.product()[num].click()

    def category_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".categoryTitle")

    def category_name(self):
        return self.category_element().text