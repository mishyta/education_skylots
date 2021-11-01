import allure
from selenium.webdriver.common.by import By

from pages.basepage import BasePage


# noinspection SpellCheckingInspection
class NavigationBar(BasePage):
    AUCTION = (By.CSS_SELECTOR, "ul.fullsize [href='/aukcion/']")
    HELP = (By.CSS_SELECTOR, "ul.fullsize [href='/faq.php']")
    PROMO = (By.CSS_SELECTOR, 'ul.fullsize [href="/faq.php?opt=poyo"]')

    LOGIN = (By.CSS_SELECTOR, ".fullsize.menu [href='/login.php']")
    REGISTRATION = (By.CSS_SELECTOR, ".fullsize.menu [href='/register.php']")
    SELL = (By.CSS_SELECTOR, ".fullsize.menu [href='/sell.php']")
    MASSEGES = (By.CSS_SELECTOR, '.fullsize.menu [href="/cabinet.php?opt=inbox"]')

    LANG_SELECTOR = (By.CSS_SELECTOR, ".fullsize.menu #headlang")
    LANG_TO_SWITCHED = (By.CSS_SELECTOR, "div.toppopmenu a[style]")

    @allure.step('Navigation bar > click option')
    def click_option(self, option):
        self.click_on_element(*option)


    def switch_lang(self):
        self.click_on_element(*NavigationBar.LANG_SELECTOR)
        self.click_on_element(*NavigationBar.LANG_TO_SWITCHED)
