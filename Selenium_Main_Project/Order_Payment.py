from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Order_Payment:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def registration_from_cart(self):
        return self.driver.find_element(By.ID,"registration_btnundefined")

    def from_shipping_to_payment(self):
        return self.driver.find_element(By.ID,'next_btn')

    def payment_method_safepay(self):
        return self.driver.find_element(By.CSS_SELECTOR,'input[name="safepay"]')

    def payment_method_masterCredit(self):
        return self.driver.find_element(By.CSS_SELECTOR,'input[name="masterCredit"]')

    def safepay_username(self):
        return self.driver.find_element(By.CSS_SELECTOR,'input[name="safepay_username"]')

    def safepay_password(self):
        return self.driver.find_element(By.CSS_SELECTOR,'input[name="safepay_password"]')

    def pay_now_safepay(self):
        return self.driver.find_element(By.ID,"pay_now_btn_SAFEPAY")

    def username_from_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR,'input[name="usernameInOrderPayment"]')

    def password_from_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR,'input[name="passwordInOrderPayment"]')

    def login_button_cart(self):
        return self.driver.find_element(By.ID,'login_btnundefined')

    def card_number(self):
        return self.driver.find_element(By.ID,'creditCard')

    def cvv_number(self):
        return self.driver.find_element(By.CSS_SELECTOR,'input[name="cvv_number"]')

    def mm_expiration_date(self):
        return self.driver.find_element(By.CSS_SELECTOR,'select[name="mmListbox"]')

    def yyyy_expiration_date(self):
        return self.driver.find_element(By.CSS_SELECTOR,'select[name="yyyyListbox"]')

    def cardholder_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="cardholder_name"]')

    def pay_now_credit(self):
        return self.driver.find_element(By.ID, 'pay_now_btn_ManualPayment')

    def after_payment_text(self):
        return self.driver.find_element(By.CSS_SELECTOR,'div>h2>span')

    def remove_order(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'tr>td>span>a')

    def edit_card(self):
        return self.driver.find_element(By.CLASS_NAME,"edit")

    def wait_after_payment_text(self):
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div>h2>span'), "Thank you for buying with Advantage"))

    # def wait_for_card_num(self):
    #     self.wait.until(EC.text_to_be_present_in_element((By.ID,'creditCard'),))

