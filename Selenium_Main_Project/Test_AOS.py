from unittest import TestCase
from Category import *
from HomePage import *
from Account import *
from Product import *
from Shopping_Cart import *
from Order_Payment import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import random


class TestAccount(TestCase):
    def setUp(self):
        print("setUp")
        service = Service(r"C:\Selenium\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 15)
        self.home_page = HomePage(self.driver)
        self.account = Account(self.driver)
        self.category = Category(self.driver)
        self.product = Product(self.driver)
        self.shopping_cart = ShoppingCart(self.driver)
        self.order_payment = OrderPayment(self.driver)


    def tearDown(self):
        print("tearDown")
        sleep(2)
        self.home_page.logo().click()
        self.driver.close()


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

        self.assertEqual(self.product.item_num_in_cart(), 6)


    # add 3 products to cart and check if their details appear in the shopping-cart popUp
    def test2(self):
        self.home_page.headphones().click()
        self.category.click_on_product(-1)
        headphone_price = self.product.item_price()
        headphone_name = self.product.product_name()
        headphone_color = self.product.colors()[-1].get_attribute("title")
        self.product.choose_color(-1)
        for i in range(3):
            self.product.quantity_plus().click()
        headphone_quantity = int(self.product.quantity().get_attribute("value"))
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.speakers().click()
        self.category.click_on_product(1)
        speaker_price = self.product.item_price()
        speaker_name = self.product.product_name()
        speaker_color = self.product.colors()[0].get_attribute("title")
        for i in range(2):
            self.product.quantity_plus().click()
        speaker_quantity = int(self.product.quantity().get_attribute("value"))
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.laptops().click()
        self.category.click_on_product(1)
        laptop_price = self.product.item_price()
        laptop_name = self.product.product_name()
        laptop_color = self.product.colors()[0].get_attribute("title")
        self.product.quantity_plus().click()
        laptop_quantity = int(self.product.quantity().get_attribute("value"))
        self.product.add_to_cart().click()

        self.assertEqual(headphone_name, self.product.text_name_prod_in_cart(-1))
        self.assertIn(speaker_name[:20], self.product.text_name_prod_in_cart(1))
        self.assertIn(laptop_name[:20], self.product.text_name_prod_in_cart(0))
        self.assertEqual(headphone_quantity, self.product.quantity_of_product_in_cart(2))
        self.assertEqual(speaker_quantity, self.product.quantity_of_product_in_cart(1))
        self.assertEqual(laptop_quantity, self.product.quantity_of_product_in_cart(0))
        self.assertEqual(laptop_color, self.product.color_of_product_in_cart(0))
        self.assertEqual(speaker_color, self.product.color_of_product_in_cart(1))
        self.assertEqual(headphone_color, self.product.color_of_product_in_cart(2))
        self.assertEqual(headphone_price * self.product.quantity_of_product_in_cart(2), self.product.total_item_price(2))
        self.assertEqual(speaker_price * self.product.quantity_of_product_in_cart(1), self.product.total_item_price(1))
        self.assertEqual(laptop_price * self.product.quantity_of_product_in_cart(0), self.product.total_item_price(0))
        self.assertEqual(self.product.total_price(), self.product.total_item_price(0) + self.product.total_item_price(1) + self.product.total_item_price(2))


    # add at least 2 products to cart, remove one and check that it's not in cart anymore
    def test3(self):
        self.home_page.headphones().click()
        self.category.click_on_product(-1)
        headphone = self.product.product_name()
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.tablets().click()
        self.category.click_on_product(-1)
        tablet = self.product.product_name()
        self.product.add_to_cart().click()
        self.assertEqual(self.product.text_name_prod_in_cart(1), headphone)
        self.assertEqual(self.product.text_name_prod_in_cart(0), tablet)
        self.assertEqual(len(self.product.x_button_in_cart()), 2)
        self.product.remove_item_from_cart(0)

        self.assertEqual(len(self.product.x_button_in_cart()), 1)
        self.assertNotEqual(self.product.text_name_prod_in_cart(0), tablet)


    # add product to cart and move to shopping-cart page
    def test4(self):
        self.home_page.laptops().click()
        self.category.click_on_product(3)
        self.product.add_to_cart().click()
        self.product.hover_cart().click()

        self.assertEqual(self.shopping_cart.shopping_text(), "SHOPPING CART")


    # add at least 3 products to cart and check if the sum of their prices is equal to total price in shopping cart page
    def test5(self):
        self.home_page.tablets().click()
        self.category.click_on_product(2)
        tablet_price = self.product.item_price()
        tablet_name = self.product.product_name()
        self.product.choose_color(-1)
        for i in range(5):
            self.product.quantity_plus().click()
        tablet_quantity = int(self.product.quantity().get_attribute("value"))
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.mice().click()
        self.category.click_on_product(-3)
        mice_price = self.product.item_price()
        mice_name = self.product.product_name()
        self.product.choose_color(1)
        for i in range(4):
            self.product.quantity_plus().click()
        mice_quantity = int(self.product.quantity().get_attribute("value"))
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.laptops().click()
        self.category.click_on_product(-2)
        laptop_price = self.product.item_price()
        laptop_name = self.product.product_name()
        self.product.quantity_plus().click()
        laptop_quantity = int(self.product.quantity().get_attribute("value"))
        self.product.add_to_cart().click()
        self.home_page.shopping_cart().click()
        self.shopping_cart.wait_text_shopping_cart()
        total_price = tablet_quantity * tablet_price + mice_price * mice_quantity + laptop_quantity * laptop_price
        print(f"product: {tablet_name}, quantity: {tablet_quantity}, price: {tablet_price}")
        print(f"product: {mice_name}, quantity: {mice_quantity}, price: {mice_price}")
        print(f"product: {laptop_name}, quantity: {laptop_quantity}, price: {laptop_price}")

        self.assertEqual(total_price, self.shopping_cart.total_price())


    # add 2 products, edit their quantities and check if the cart has been updated
    # bug in the site!!!!!!!
    def test6(self):
        self.home_page.tablets().click()
        self.category.click_on_product(1)
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.mice().click()
        self.category.click_on_product(4)
        self.product.add_to_cart().click()
        self.home_page.shopping_cart().click()
        self.shopping_cart.edit_product(1).click()
        for i in range(2):
            self.product.quantity_plus().click()
        mice_quantity = int(self.product.quantity().get_attribute("value"))
        self.product.add_to_cart().click()
        self.shopping_cart.edit_product(1).click()
        for i in range(5):
            self.product.quantity_plus().click()
        tablet_quantity = int(self.product.quantity().get_attribute("value"))
        self.product.add_to_cart().click()
        self.home_page.shopping_cart().click()

        self.assertEqual(self.shopping_cart.product_quantity(1), mice_quantity)
        self.assertEqual(self.shopping_cart.product_quantity(0), tablet_quantity)


    # after choosing a tablet go back to tablets and then go back to home page
    def test7(self):
        self.home_page.tablets().click()
        tablets = self.category.category_name()
        self.category.click_on_product(1)
        self.product.add_to_cart().click()
        self.driver.back()
        self.assertTrue(self.category.category_name() == tablets)
        self.driver.back()
        self.assertEqual(self.home_page.mice().text, "MICE")


    # checkout product, create new account and pay with safepay. check that the cart is empty and order appear in orders page
    def test8(self):
        self.home_page.tablets().click()
        self.category.click_on_product(0)
        self.product.choose_color(1)
        self.product.add_to_cart().click()
        self.home_page.shopping_cart().click()
        self.shopping_cart.checkout_btn().click()
        self.order_payment.registration().click()
        self.account.username().send_keys("NewUser")
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
        self.order_payment.next_btn().click()
        self.order_payment.payment_method_safepay().click()
        self.order_payment.safepay_username().send_keys("username")
        self.order_payment.safepay_password().send_keys("Password34")
        self.order_payment.pay_now_safepay().click()
        # to see if the purchase was successful
        self.order_payment.wait_after_payment_text()
        order_number = self.order_payment.order_number_text()
        self.assertEqual(self.order_payment.after_payment_text().text, "Thank you for buying with Advantage")
        self.home_page.shopping_cart().click()
        # check if the shopping cart is empty
        self.shopping_cart.wait_until_text_cart_empty()
        self.assertEqual(self.shopping_cart.shopping_cart_empty().text, "Your shopping cart is empty")
        self.shopping_cart.wait_until_text_cart_empty()
        self.home_page.user().click()
        self.home_page.my_orders_btn().click()
        while True:
            try:
                self.home_page.my_orders_btn().click()
                break
            except:
                pass
        # check if the order is in the user orders
        self.assertEqual(order_number, self.shopping_cart.order_number())
        while True:
            try:
                self.home_page.user().click()
                self.home_page.my_account_btn().click()
                break
            except:
                pass
        self.account.confirm_delete().click()


    # checkout item with an existence account paying with creditCard and check for empty cart and order appear in orders page
    def test9(self):
        self.home_page.mice().click()
        self.category.click_on_product(0)
        self.product.add_to_cart().click()
        self.home_page.shopping_cart().click()
        self.shopping_cart.checkout_btn().click()
        self.order_payment.username().send_keys("Muigadol111")
        self.order_payment.password().send_keys('Muigadol111')
        self.order_payment.login_btn().click()
        self.order_payment.next_btn().click()
        self.order_payment.edit_btn().click()
        self.order_payment.card_number().clear()
        self.order_payment.cvv_number().clear()
        while len(self.order_payment.cvv_number().get_attribute("value")) != 3:
            self.order_payment.cvv_number().send_keys('1')
        self.order_payment.cvv_number().clear()
        while len(self.order_payment.cvv_number().get_attribute("value")) != 3:
            self.order_payment.cvv_number().send_keys('1')
        self.order_payment.expiration_month().send_keys("10")
        self.order_payment.expiration_year().send_keys("2028")
        self.order_payment.card_number().send_keys('123456789123')
        self.order_payment.pay_now_btn().click()
        self.order_payment.wait_order_number()
        order_number = self.order_payment.order_number_text()
        self.shopping_cart.wait_until_cart_empty()
        self.home_page.shopping_cart().click()
        self.shopping_cart.wait_until_text_cart_empty()
        self.assertEqual(self.shopping_cart.shopping_cart_empty().text, "Your shopping cart is empty")
        self.home_page.click_my_order_btn()
        self.shopping_cart.wait_order_number()
        self.assertEqual(order_number, self.shopping_cart.order_number())
        self.shopping_cart.remove_order().click()
        self.shopping_cart.approve_remove().click()


    # login with existence user and then logout
    def test10(self):
        self.home_page.user().click()
        self.account.popUp_username().send_keys("BasaLo")
        username = self.account.popUp_username().get_attribute("value")
        self.account.popUp_password().send_keys("Tester1")
        self.account.click_sign_in()
        self.wait.until(EC.visibility_of(self.home_page.mice()))
        self.assertEqual(self.account.loggedIn_username().text, username)
        self.home_page.click_sign_out_btn()
        self.account.wait_username_text()
        self.assertEqual(self.account.loggedIn_username().text, "")










