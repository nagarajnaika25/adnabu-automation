from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class AdNabuAutomation:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)

    def open_store(self):
        self.driver.get("https://adnabu-store-assignment1.myshopify.com/")

        password = self.wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password.send_keys("AdNabuQA")
        password.send_keys(Keys.ENTER)

        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    def search_product(self, product_name):
        search_icon = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "summary.header__icon--search"))
        )
        search_icon.click()

        search_box = self.wait.until(
            EC.presence_of_element_located((By.ID, "Search-In-Modal"))
        )
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.ENTER)

        time.sleep(2)

        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.full-unstyled-link"))
        )

    def open_product(self):
        products = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "a.full-unstyled-link[href*='/products/']")
            )
        )

        for p in products:
            if p.is_displayed():
                self.driver.execute_script("arguments[0].click();", p)
                break

    def add_to_cart(self):
        add_cart = self.wait.until(
            EC.element_to_be_clickable((By.NAME, "add"))
        )
        add_cart.click()
    

    def verify_cart(self):
        cart_icon = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-count-bubble"))
        )
        assert cart_icon.is_displayed()
        print("Product successfully added to cart and verified")

    def close(self):
        time.sleep(2)
        self.driver.quit()


#PYTEST TEST CASE
def test_search_add_cart():
    test = AdNabuAutomation()
    test.open_store()
    test.search_product("Snowboard")
    test.open_product()
    test.add_to_cart()
    test.verify_cart()
    test.close()
