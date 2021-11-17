from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Product:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def colors(self):
        rabbit = self.driver.find_elements(By.ID, 'rabbit')
        bunny = self.driver.find_elements(By.ID, 'bunny')
        if len(bunny) == 0:
            return rabbit
        else:
            return bunny

    def choose_color(self, num):
        self.colors()[num].click()

    def item_price(self):
        return float(self.driver.find_element(By.CSS_SELECTOR, "#Description>h2").get_attribute("innerHTML")[2:-158])

    def quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[name='quantity']")

    def quantity_plus(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.plus')

    def add_to_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="save_to_cart"]')

    def hover_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, "span>label")

    def item_num_in_cart(self):
        return int(self.hover_cart().get_attribute("innerHTML")[1])

    def items_in_cart(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "tbody>tr")

    def name_product_in_cart(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "td>a>h3")

    def text_name_prod_in_cart(self, num):
        return self.name_product_in_cart()[num].get_attribute("innerHTML")

    def quantity_of_product_in_cart(self, number):
        quantity_list = self.driver.find_elements(By.CSS_SELECTOR, "a>label")
        for i in quantity_list:
            if "QTY" not in i.get_attribute("innerHTML"):
                quantity_list.remove(i)
        quantity_list.reverse()
        return int(quantity_list[number].get_attribute("innerHTML")[5:])

    def color_of_product_in_cart(self, number):
        colors = self.driver.find_elements(By.CSS_SELECTOR, "a>label>span")
        colors.reverse()
        return colors[number].get_attribute("innerHTML")

    def total_item_price(self, num):
        prices = self.driver.find_elements(By.CSS_SELECTOR, '[class="price roboto-regular ng-binding"]')
        prices.reverse()
        return float(prices[num].get_attribute("innerHTML")[1:])

    def total_price(self):
        total_price = self.driver.find_element(By.CSS_SELECTOR, '[class="roboto-medium cart-total ng-binding"]')
        return float(total_price.get_attribute("innerHTML")[1:])

    def x_button_in_cart(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '[class="removeProduct iconCss iconX"]')

    def remove_item_from_cart(self, number):
        self.x_button_in_cart()[number].click()

    def back_to_products(self):
        return self.driver.find_element(By.CSS_SELECTOR,'a[class="ng-binding"]')

    def go_to_cart(self):
        return self.driver.find_element(By.ID,"menuCart")









# class Inside_Product:
#
#     def __init__(self,driver : webdriver):
#         self.driver=driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def choose_color(self,color):
#         color = self.driver.find_elements(By.ID, 'rabbit')
#         color[-1].click()
#
#     def choose_quantity(self,quantity):
#         product_quantity=self.driver.find_element(By.CSS_SELECTOR,"input[name='quantity']")
#         product_quantity.click()
#         product_quantity.send_keys(Keys.DELETE)
#         product_quantity.send_keys(quantity)
#
#     def add_to_cart(self):
#         add_button= self.driver.find_element(By.CSS_SELECTOR,"button[name='save_to_cart']")
#         add_button.click()















