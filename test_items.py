import time

def test_find_add_to_card_btn(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/hackers-painters_185/')
    time.sleep(10)
    # res = browser.find_element_by_css_selector("button[class='btn btn-lg btn-primary btn-add-to-basket']")
    basket = browser.find_element_by_css_selector("form button.btn-add-to-basket")
    assert basket.text, "Element not found"
    print(basket.text)
