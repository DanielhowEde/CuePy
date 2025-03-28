from selenium.webdriver.common.by import By
from src.core.BasePage import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    DASHBOARD = (By.ID, "dashboard")

    def go_to_login(self, url="http://example.com/login"):
        self.driver.get(url)

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def is_dashboard_visible(self):
        return self.is_visible(self.DASHBOARD)