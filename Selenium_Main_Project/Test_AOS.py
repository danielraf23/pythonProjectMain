from unittest import TestCase
from Category import *
from HomePage import *
from Account import *
from Product import *
from Order_Payment import *
from Shopping_Cart import *
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import random
from selenium.webdriver import ActionChains



class TestAccount(TestCase):
    def setUp(self):
        print("setUp")
        service = Service(r"C:\Selenium\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        self.home_page = HomePage(self.driver)
        self.account = Account(self.driver)
        self.category = Category(self.driver)
        self.product = Product(self.driver)
        self.order_payment = Order_Payment(self.driver)
        self.shopping_cart = Shopping_cart(self.driver)
        self.actionChains = ActionChains(self.driver)

    # add 2 products in different quantities that bigger then 1, and check the total number of items in cart
    def test1(self):
        self.home_page.mice().click()
        self.category.click_on_product(1)
        self.product.choose_color(1)
        for i in range(3):
            self.product.quantity_plus().click()
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.laptops().click()
        self.category.click_on_product(-2)
        self.product.quantity_plus().click()
        self.product.add_to_cart().click()

        self.assertEqual(self.product.item_num_in_cart(), "6")

        # add 3 products to cart and check if their details appear in the shopping-cart popUp

    def test2(self):
        self.home_page.headphones().click()
        self.category.click_on_product(2)
        headphone_price = self.product.item_price()
        self.product.choose_color(-1)
        for i in range(3):
            self.product.quantity_plus().click()
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.speakers().click()
        self.category.click_on_product(1)
        speaker_price = self.product.item_price()
        for i in range(2):
            self.product.quantity_plus().click()
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.laptops().click()
        self.category.click_on_product(-2)
        laptop_price = self.product.item_price()
        self.product.quantity_plus().click()
        self.product.add_to_cart().click()

        self.assertEqual("HP H2310 IN-EAR HEADSET", self.product.text_name_prod_in_cart(-1))
        self.assertIn("BOSE SOUNDLINK WIRELESS", self.product.text_name_prod_in_cart(1))
        self.assertEqual("HP STREAM - 11-D020NR LAPTOP", self.product.text_name_prod_in_cart(0))
        self.assertEqual(4, self.product.quantity_of_product_in_cart(0))
        self.assertEqual(3, self.product.quantity_of_product_in_cart(1))
        self.assertEqual(2, self.product.quantity_of_product_in_cart(2))
        self.assertEqual("YELLOW", self.product.color_of_product_in_cart(0))
        self.assertEqual("TURQUOISE", self.product.color_of_product_in_cart(1))
        self.assertEqual("PURPLE", self.product.color_of_product_in_cart(2))
        self.assertEqual(headphone_price * self.product.quantity_of_product_in_cart(0),
                         self.product.total_item_price(0))
        self.assertEqual(speaker_price * self.product.quantity_of_product_in_cart(1), self.product.total_item_price(1))
        self.assertEqual(laptop_price * self.product.quantity_of_product_in_cart(2), self.product.total_item_price(2))
        self.assertEqual(self.product.total_price(), self.product.total_item_price(0) + self.product.total_item_price(
            1) + self.product.total_item_price(2))

        # add at least 2 products to cart, remove one and check that it's not in cart anymore

    def test3(self):
        self.home_page.headphones().click()
        self.category.click_on_product(-1)
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.tablets().click()
        self.category.click_on_product(-1)
        self.product.add_to_cart().click()
        self.assertEqual(self.product.text_name_prod_in_cart(1), "LOGITECH USB HEADSET H390")
        self.assertEqual(len(self.product.x_button_in_cart()), 2)
        self.product.remove_item_from_cart(1)

        self.assertEqual(len(self.product.x_button_in_cart()), 1)
        self.assertEqual(self.product.text_name_prod_in_cart(0), "HP PRO TABLET 608 G1")

        # add product to cart and move to shopping-cart page

    def test4(self):
        self.home_page.laptops().click()
        self.category.click_on_product(3)
        self.product.add_to_cart().click()
        self.product.hover_cart().click()

        self.assertEqual(self.shopping_cart.shopping_text(), "SHOPPING CART")

    def test5(self):
        self.home_page.laptops().click()
        self.category.click_on_product(3)
        price = self.product.item_price()
        self.product.add_to_cart().click()
        self.product.hover_cart().click()
        print(price + 1)


    def tests7(self):
        self.home_page.tablets().click()
        self.category.click_on_product(0)
        self.product.choose_color(1)
        self.product.add_to_cart().click()
        self.product.back_to_products().click()
        self.assertEqual(self.category.get_into_product(),self.driver.find_elements(By.CSS_SELECTOR, "[class ='cell categoryRight'] > ul > li"))
        self.category.back_to_homepage().click()
        self.assertEqual(self.home_page.mice(),self.driver.find_element(By.ID, 'miceImg'))



# sign in with new user from shopping cart, buy the product and then check if the shopping cart is empty
# and if the product bought is in orders
    def test8(self):
        self.home_page.tablets().click()
        self.category.click_on_product(0)
        self.product.choose_color(1)
        self.product.add_to_cart().click()
        self.product.go_to_cart().click()
        self.shopping_cart.checkout().click()
        self.order_payment.registration_from_cart().click()
        self.account.username().send_keys("user12")
        self.account.email().send_keys("email@gmail.com")
        self.account.password().send_keys("Pass2")
        self.account.confirm_password().send_keys("Pass2")
        self.account.first_name().send_keys('First')
        self.account.last_name().send_keys("Last")
        self.account.country().send_keys('Israel')
        self.account.city().send_keys("sderot")
        self.account.address().send_keys("struma 1")
        self.account.state().send_keys("hadarom")
        self.account.postal_code().send_keys("1234234")
        self.account.agree_conditions().click()
        self.account.register_btn().click()
        self.order_payment.from_shipping_to_payment().click()
        self.order_payment.payment_method_safepay().click()
        self.order_payment.safepay_username().send_keys("username")
        self.order_payment.safepay_password().send_keys("Password34")
        self.order_payment.pay_now_safepay().click()
        #to see if the purchase was sucssesful
        self.order_payment.wait_after_payment_text()
        self.assertEqual(self.order_payment.after_payment_text().text, "Thank you for buying with Advantage")
        self.product.go_to_cart().click()
        # check if the shopping cart is empty
        self.assertEqual(self.shopping_cart.shopping_cart_is_empty().text, "Your shopping cart is empty")
        self.account.user_manu_2().click()
        while True:
            try:
                self.account.my_orders().click()
                break
            except:
                pass
        # check if the order is in the user orders
        self.assertEqual(self.order_payment.remove_order().text, "REMOVE")
        self.account.user_manu_2().click()
        self.account.user_menu().click()
        self.account.delete_account().click()
        self.account.confirm_delete().click()



    def test9(self):
        self.home_page.tablets().click()
        self.category.click_on_product(0)
        self.product.choose_color(1)
        self.product.add_to_cart().click()
        self.product.go_to_cart().click()
        self.shopping_cart.checkout().click()
        self.order_payment.username_from_cart().send_keys("danidin")
        self.order_payment.password_from_cart().send_keys('Raf369')
        self.order_payment.login_button_cart().click()
        self.order_payment.from_shipping_to_payment().click()
        self.order_payment.payment_method_masterCredit().click()
        self.order_payment.edit_card().click()
        self.order_payment.card_number().clear()
        self.order_payment.card_number().send_keys('123456789123')
        self.order_payment.cvv_number().clear()
        while len(self.order_payment.cvv_number().get_attribute("value")) != 3:
            self.order_payment.cvv_number().send_keys('1')
        self.order_payment.mm_expiration_date().send_keys('07')
        self.order_payment.yyyy_expiration_date().send_keys('2023')
        self.order_payment.cardholder_name().clear()
        self.order_payment.cardholder_name().send_keys('Daniel Rafailsky')
        self.order_payment.pay_now_credit().click()
        sleep(10)
        # while True:
        #     try:
        #         self.order_payment.pay_now_credit().click()
        #         break
        #     except:
        #         pass

        # self.order_payment.pay_now_credit().click()
        # self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div>h2>span'), 'Thank you for buying with Advantage'))
        # self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, 'div>h2>span').text, "Thank you for buying with Advantage")
        # self.product.go_to_cart().click()
        # text = self.driver.find_element(By.CSS_SELECTOR, ".bigEmptyCart>label").text
        # self.assertEqual(text, "Your shopping cart is empty")
        # self.account.user_manu_2().click()
        # while True:
        #     try:
        #         self.account.my_orders().click()
        #         break
        #     except:
        #         pass
        # self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, 'tr>td>span>a').text, "REMOVE")
        # self.category.back_to_homepage().click()






    def test10(self):
        self.home_page.user().click()
        self.account.popUp_username().send_keys("daniel")
        self.account.popUp_password().send_keys("Raf369")
        self.account.signIn_button().click()
        # self.assertEqual(self.account.user_menu_options(0), "My account")
        self.wait.until(EC.element_to_be_clickable((By.ID, 'speakersImg')))
        self.home_page.click_sign_out_btn()
        sleep(3)
        self.driver.find_element(By.ID, "menuUserLink").click()
        self.assertEqual(self.account.validation_of_logout().text, 'Username')

    # self.home_page.user().click()
    # self.account.popUp_username().send_keys("BasaLo")
    # self.account.popUp_password().send_keys("Tester1")
    # self.account.signIn_button().click()
    # self.assertEqual(self.account.user_menu_options(0), "My account")
    # self.wait.until(EC.element_to_be_clickable((By.ID, 'speakersImg')))
    # self.home_page.user().click()
    # self.home_page.sign_out_btn().click()

    def tearDown(self) :
        sleep(5)
        print("tearDown")
        #self.driver.close()











