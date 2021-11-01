import allure
from selenium.webdriver.common.by import By

from pages.basepage import BasePage
from utils.crds import crds
from utils.rndm import CreedsGenerator


class LoginPage(BasePage):
    # Creeds
    VALID_CREEDS = crds.get()
    INVALID_CREEDS = ('invalidlogin', CreedsGenerator.generate_pswrd(8))

    # elements locators:
    LOGIN_FIELD = (By.CSS_SELECTOR, "[name='user_login']")
    PSWRD_FIELD = (By.CSS_SELECTOR, "[name='user_password']")
    LOGIN_BTN = (By.CSS_SELECTOR, '#fullsize_description .green_button.login_button')
    ELEMENT_TO_SUCCES_LOGIN_SUCCESFUL = (By.CSS_SELECTOR, '.fullsize.menu [href="/cabinet.php"]')
    ELEMENT_TO_SUCCES_LOGIN_UNSUCCESFUL = (By.CSS_SELECTOR, '#fullsize_description [href="mailto:support@skylots.org"]')

    def login(self, login, pswrd, valid=True):

        # valid = True/False tell us which credentials are used
        #

        with allure.step('Input creeds:'):
            self.write_to_element(*LoginPage.LOGIN_FIELD, login)
            self.write_to_element(*LoginPage.PSWRD_FIELD, pswrd)
        with allure.step('Submit:'):
            self.click_on_element(*LoginPage.LOGIN_BTN)
        with allure.step('Check login status:'):
            if valid:
                assert self.check_element_exist(*LoginPage.ELEMENT_TO_SUCCES_LOGIN_SUCCESFUL)
            else:
                assert self.check_element_exist(*LoginPage.ELEMENT_TO_SUCCES_LOGIN_UNSUCCESFUL)
