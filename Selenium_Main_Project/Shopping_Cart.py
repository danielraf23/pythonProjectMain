from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ShoppingCart:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def shopping_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class="select  ng-binding"]').get_attribute("innerHTML")[1:]

    def product_quantity(self, number):
        quantity_list = self.driver.find_elements(By.CSS_SELECTOR, '#shoppingCart>table>tbody>tr>td>label[class="ng-binding"]')
        return int(quantity_list[number].text)

    def product_color(self, number):
        colors = self.driver.find_elements(By.CLASS_NAME, "productColor")
        return colors[number].get_attribute("title")

    def total_price(self):
        price = self.driver.find_element(By.CSS_SELECTOR, '#shoppingCart>table>tfoot>tr>td>span[class="roboto-medium ng-binding"]').text
        if len(price) < 8:
            return float(price[1:])
        elif len(price) == 9:
            return float(price[1] + price[3:])
        else:
            return float(price[1:2] + price[4:])

    # return the edit button of input index
    def edit_product(self, number):
        return self.driver.find_elements(By.CSS_SELECTOR, '[translate="EDIT"]')[number]

    def wait_text_shopping_cart(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="select  ng-binding"]')))

    def checkout_btn(self):
        return self.driver.find_element(By.ID, "checkOutButton")

    def shopping_cart_empty(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class="roboto-bold ng-scope"]')

    def wait_until_text_cart_empty(self):
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class="roboto-bold ng-scope"]'), "Your shopping cart is empty"))

    def wait_until_cart_empty(self):
        self.wait.until_not(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#shoppingCartLink>span'), "1"))

    def first_row(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '.cover>table>tbody>tr>td>label[class="ng-binding"]')

    def order_number(self):
        return self.first_row()[0].text

    def wait_order_number(self):
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class="roboto-regular sticky fixedImportant ng-scope"]'), "MY ORDERS"))

    def remove_order(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[translate="REMOVE"]')

    def approve_remove(self):
        return self.driver.find_element(By.ID, 'confBtn_1')