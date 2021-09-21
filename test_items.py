from selenium import webdriver
import time
def test_items(browser):

    browser.implicitly_wait(5)
    button = browser.find_element_by_css_selector('.btn.btn-add-to-basket')
    check_button = button.get_attribute('type')
    assert check_button == 'submit', '<<< button not found >>>'