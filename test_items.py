from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_is_button_has(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, '[id="add_to_basket_form"] button')
