from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def speakers(self):
        return self.driver.find_element(By.ID, 'speakersImg')

    def tablets(self):
        return self.driver.find_element(By.ID, 'tabletsImg')

    def laptops(self):
        return self.driver.find_element(By.ID, 'laptopsImg')

    def mice(self):
        return self.driver.find_element(By.ID, 'miceImg')

    def headphones(self):
        return self.driver.find_element(By.ID, 'headphonesImg')

    def logo(self):
        return self.driver.find_element(By.CLASS_NAME, 'logo')

    def user(self):
        return self.driver.find_element(By.ID, 'menuUserLink')

    def create_user(self):
        self.wait.until(EC.text_to_be_present_in_element((By.LINK_TEXT, "CREATE NEW ACCOUNT"), "CREATE NEW ACCOUNT"))
        return self.driver.find_element(By.LINK_TEXT, "CREATE NEW ACCOUNT")

    def shopping_cart(self):
        return self.driver.find_element(By.ID, 'shoppingCartLink')

    def my_account_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class="option ng-scope"][translate="My_account"]')

    def click_my_account_btn(self):
        self.user().click()
        self.my_account_btn().click()

    def my_orders_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.mobileTitle>div>[class="option ng-scope"][translate="My_Orders"]')

    def click_my_order_btn(self):
        self.user().click()
        self.my_orders_btn().click()

    def sign_out_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[translate='Sign_out'][class='option roboto-medium ng-scope']")

    def click_sign_out_btn(self):
        self.user().click()
        self.sign_out_btn().click()