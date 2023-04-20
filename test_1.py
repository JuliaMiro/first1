from selenium.webdriver.common.by import By
import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



def test_open_page():
    driver.get('https://openweathermap.org/')
    assert "openweathermap" in driver.current_url
    print(driver.current_url)

def test_check_page_title():
    driver.get('https://openweathermap.org/')
    assert driver.title == "Сurrent weather and forecast - OpenWeatherMap"

def test_fill_search_city_title():
    driver.get('https://openweathermap.org/')
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys("New York")
    time.sleep(5)
    search_button = driver.find_element(By.CSS_SELECTOR, 'button[class = "button-round dark"]')
    search_button.click()
    search_option = driver.find_element(By.CSS_SELECTOR, )




# def test_open():
#     driver.get('https://suninjuly.github.io/xpath_examples')
#     time.sleep(5)
#
# def test_find_cat():
#     driver.get('http://suninjuly.github.io/cats.html')
#     time.sleep(3)
#     cat = driver.find_element(By.XPATH, '//*[contains(text(), "Bullet cat")]')
#     print(cat.text)