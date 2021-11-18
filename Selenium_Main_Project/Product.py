from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Product:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # return the name of a product
    def product_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#Description>h1").text

    # return a list of all available colors for product
    def colors(self):
        rabbit = self.driver.find_elements(By.ID, 'rabbit')
        bunny = self.driver.find_elements(By.ID, 'bunny')
        if len(bunny) == 0:
            return rabbit
        else:
            return bunny

    # get a num of color in the list and click on it
    def choose_color(self, num):
        self.colors()[num].click()

    # return the price of product as float. if "," exists - remove
    def item_price(self):
        if len(self.driver.find_element(By.CSS_SELECTOR, "#Description>h2").text) < 9:
            return float(self.driver.find_element(By.CSS_SELECTOR, "#Description>h2").text[1:])
        else:
            return float(self.driver.find_element(By.CSS_SELECTOR, "#Description>h2").text[1] + self.driver.find_element(By.CSS_SELECTOR, "#Description>h2").text[3:])

    # return the quantity element
    def quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[name='quantity']")

    # return the plus button of quantity
    def quantity_plus(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.plus')

    # return the add to cart button
    def add_to_cart(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[name="save_to_cart"]')))
        return self.driver.find_element(By.CSS_SELECTOR, '[name="save_to_cart"]')

    # return the cart shopping icon element in top right
    def hover_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, "span>label")

    # return the number of items in cart as int
    def item_num_in_cart(self):
        return int(self.hover_cart().get_attribute("innerHTML")[1])

    # return list of product in cart
    def items_in_cart(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "tbody>tr")

    # return list of the names of products in cart
    def name_product_in_cart(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "td>a>h3")

    # get a number and return the text of it's name on the list
    def text_name_prod_in_cart(self, num):
        return self.name_product_in_cart()[num].text

    # get a number and return the quantity of it's index in the list, as int
    def quantity_of_product_in_cart(self, number):
        quantity_list = self.driver.find_elements(By.CSS_SELECTOR, "a>label")
        for i in quantity_list:
            if "QTY" not in i.get_attribute("innerHTML"):
                quantity_list.remove(i)
        return int(quantity_list[number].get_attribute("innerHTML")[5:])

    # get a number and return the color of it's index on the list
    def color_of_product_in_cart(self, number):
        colors = self.driver.find_elements(By.CSS_SELECTOR, "a>label>span")
        return colors[number].get_attribute("innerHTML")

    # get a number and return the total price of the index product in cart
    def total_item_price(self, num):
        prices = self.driver.find_elements(By.CSS_SELECTOR, '[class="price roboto-regular ng-binding"]')
        if len(prices[num].get_attribute("innerHTML")) <= 7:
            return float(prices[num].get_attribute("innerHTML")[1:])
        else:
            return float(prices[num].get_attribute("innerHTML")[1] + prices[num].get_attribute("innerHTML")[3:])

    # return the total price of shopping cart
    def total_price(self):
        total_price = self.driver.find_element(By.CSS_SELECTOR, '[class="roboto-medium cart-total ng-binding"]')
        if len(total_price.get_attribute("innerHTML")) <= 7:
            return float(total_price.get_attribute("innerHTML")[1:])
        else:
            return float(total_price.get_attribute("innerHTML")[1] + total_price.get_attribute("innerHTML")[3:])

    # return a list of all x-button appear in shopping cart
    def x_button_in_cart(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '[class="removeProduct iconCss iconX"]')

    # get a number and remove it's product from cart
    def remove_item_from_cart(self, number):
        self.x_button_in_cart()[number].click()














