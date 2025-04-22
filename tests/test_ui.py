import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def setup_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_product_listing(setup_driver):
    driver = setup_driver
    driver.get("http://localhost:5000")
    
    assert "Elektronik Mağazası" in driver.page_source
    
    products = driver.find_elements(By.TAG_NAME, "li")
    assert len(products) > 0
    assert "Akıllı Telefon" in driver.page_source

def test_add_to_cart(setup_driver):
    driver = setup_driver
    driver.get("http://localhost:5000")
    
    add_to_cart_button = driver.find_element(By.CLASS_NAME, "add-to-cart")
    add_to_cart_button.click()
    
    assert "Alışveriş Sepeti" in driver.title
    assert "Akıllı Telefon" in driver.page_source
