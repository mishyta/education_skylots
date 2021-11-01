from pages.mainpage import *


def test_lang_switch(driver):
    page = MainPage()
    page.open()
    page.nb.switch_lang()
