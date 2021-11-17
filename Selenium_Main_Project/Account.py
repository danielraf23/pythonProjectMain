from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.select import Select


class Account:
    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(self.driver, 10)

    def username(self):
        return self.driver.find_element(By.CSS_SELECTOR,'[name="usernameRegisterPage"]')

    def email(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="emailRegisterPage"]')

    def password(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="passwordRegisterPage"]')

    def confirm_password(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="confirm_passwordRegisterPage"]')

    def first_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="first_nameRegisterPage"]')

    def last_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="last_nameRegisterPage"]')

    def phone_number(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="phone_numberRegisterPage"]')

    def country(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="countryListboxRegisterPage"]')

    def select_country(self, country):
        select_country = Select(self.country())
        select_country.select_by_visible_text(country)

    def city(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="cityRegisterPage"]')

    def address(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="addressRegisterPage"]')

    def state(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="state_/_province_/_regionRegisterPage"]')

    def postal_code(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="postal_codeRegisterPage"]')

    def agree_conditions(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="i_agree"]')

    def register_btn(self):
        return self.driver.find_element(By.ID, 'register_btnundefined')

    def edit_account_details(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[href="#/accountDetails"]')

    def edit_payment(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[href="#/accountPaymentEdit"]')

    def popUp_username(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="username"]')

    def popUp_password(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="password"]')

    def signIn_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[type="button"]')

    def loggedIn_username(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#menuUserLink>span")

    def user_menu(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#menuUserLink>div>label")

    def user_menu_options(self, number):
        return self.user_menu()[number].get_attribute("innerHTML")

    def user_manu_2(self):
        return self.driver.find_element(By.ID,'menuUser')

    def my_orders(self):
        return self.driver.find_element(By.CSS_SELECTOR,"li>a>div>label[translate='My_Orders']")

    def delete_account(self):
        return self.driver.find_element(By.CSS_SELECTOR,'div[class="deleteBtnText"]')

    def confirm_delete(self):
        return self.driver.find_element(By.CSS_SELECTOR,'div[class="deletePopupBtn deleteRed"]')

    def regretting_delete(self):
        return self.driver.find_element(By.CSS_SELECTOR,'div[class="deletePopupBtn deleteGreen"]')

    def validation_of_logout(self):
        return self.driver.find_element(By.CSS_SELECTOR,'div[class="displayed"]')



