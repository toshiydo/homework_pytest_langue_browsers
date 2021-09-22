

def test_button_addToBasket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_element_by_css_selector('.btn.btn-add-to-basket')
    check_button = button.get_attribute('type')
    assert check_button == 'submit', '<<< button not found >>>'