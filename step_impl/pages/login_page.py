from selenium.webdriver.common.by import By
from step_impl.pages.base_page import BasePage
import time


class LoginPageLocators:
    """ This is the class for login page locators. All login page locators should come here """

    LOGIN_HEADER = (By.XPATH, "//span[.='Giriş Yap']")
    LOGIN_BUTTON = (By.ID, "login")
    USER_NAME_TEXT = (By.ID, "txtUserName")
    PASSWORD_TEXT = (By.ID, "txtPassword")
    SIGN_IN_BUTTON = (By.ID, "btnLogin")


class LoginPage(BasePage):
    URL = '{}/login'.format(BasePage.MAIN_URL)

    """ Login page actions """

    def visit(self):
        self.driver.get(self.URL)

    def login(self, user_name, password):
        self.hover(LoginPageLocators.LOGIN_HEADER)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.set(LoginPageLocators.USER_NAME_TEXT, user_name)
        self.set(LoginPageLocators.PASSWORD_TEXT, password)
        self.click(LoginPageLocators.SIGN_IN_BUTTON)
