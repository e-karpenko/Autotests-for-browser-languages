import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# в качестве параметра в скобках передается browser из conftest.py
def test_guest_should_see_btn_adding_to_basket(browser):
    browser.get(link)
    time.sleep(30)

#ищем кнопку на странице, если количество <= 0, выдаем текст с ошибкой
    amount_btn = len(browser.find_elements_by_css_selector(".btn-add-to-basket")) 
    assert amount_btn>0, f"There is no button of adding to basket"  

