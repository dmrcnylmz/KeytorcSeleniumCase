from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class HomePageLocators:
    """ This is the class for home page locators. All home page locators should come here """

    SIGN_IN_CONTROL = (By.XPATH, "//span[.='Hesabım']")

    SEARCH_BOX_INPUT = (By.CSS_SELECTOR, "div[role='combobox'] > .desktopOldAutosuggestTheme-input")
    SEARCH_CONTROL = (By.XPATH, "//h1[@class='keyword'][.='samsung']")
    SEARCH_BUTTON = (By.XPATH, "//div[@class='SearchBoxOld-buttonContainer']")
    GRID_SHORT_BUTTON = (By.CSS_SELECTOR, ".grid.sortButton")
    SECOND_PAGE_BUTTON = (By.CSS_SELECTOR, ".page-2")
    SECOND_PAGE_ACTIVE_BUTTON = (By.XPATH, "//a[@class='page-2 active']")
    THIRD_PRODUCT_HEART_BUTTON = (By.XPATH, "(//div[@id='heartWrapper'])[3]")
    FAVORITE_BUTTON = (By.XPATH, "//li/a[.='Beğendiklerim']")
    THIRD_PRODUCT_NAME = (By.XPATH, "(//div/p/span)[3]")


class HomePage(BasePage):
    """ Home page actions """

    def is_home_page_visible(self):
        assert self.is_displayed(HomePageLocators.SIGN_IN_CONTROL), "Sign in Fail"

    def searchAndControl(self,searchText):
        self.set(HomePageLocators.SEARCH_BOX_INPUT, searchText)
        self.click(HomePageLocators.SEARCH_BUTTON)
        self.is_displayed(HomePageLocators.SEARCH_CONTROL)

    def goToSecondPageAndControl(self):
        self.click(HomePageLocators.GRID_SHORT_BUTTON)
        self.do_scroll_to_element(HomePageLocators.SECOND_PAGE_BUTTON)
        self.click(HomePageLocators.SECOND_PAGE_BUTTON)
        self.is_displayed(HomePageLocators.SECOND_PAGE_ACTIVE_BUTTON)

    def addFavoriteThirdProduct(self):
        self.hover(HomePageLocators.THIRD_PRODUCT_HEART_BUTTON)
        self.click(HomePageLocators.THIRD_PRODUCT_HEART_BUTTON)

    def getProductName(self):
        FavoriteProduct1 = self.get(HomePageLocators.THIRD_PRODUCT_NAME)
        return FavoriteProduct1

    def goToFavoritePage(self):
        self.hover(HomePageLocators.SIGN_IN_CONTROL)
        self.click(HomePageLocators.FAVORITE_BUTTON)

