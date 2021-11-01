import allure

from pages.mainpage import *
from pages.loginpage import LoginPage


@allure.story('Login with invalid creeds.')
def test_login_with_invalid_crds(driver):
    page = MainPage()
    page.open()
    page.nb.click_option(NavigationBar.LOGIN)
    page = LoginPage()
    page.login(*LoginPage.INVALID_CREEDS, valid=False)


@allure.story('Login with valid creeds.')
def test_login_valid_crds(driver):
    page = MainPage()
    page.open()
    page.nb.click_option(NavigationBar.LOGIN)
    page = LoginPage()
    page.login(*LoginPage.VALID_CREEDS)
