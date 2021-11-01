from pages.basepage import BasePage
from pages.top_nav_bar import NavigationBar


class MainPage(BasePage):
    URL = 'https://skylots.org/'

    def __init__(self) -> None:
        super().__init__()
        self.nb = NavigationBar()

    def open(self):
        self.open_page(MainPage.URL)
