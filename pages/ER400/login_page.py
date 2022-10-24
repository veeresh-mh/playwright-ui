from util.logger import *

class LoginPage:
    def __init__(self,page):
        self.page = page
        self.log = get_logger()
        self.username_input = self.page.locator("//input[@name='username']")
        self.password_input = self.page.locator("//input[@name='password']")
        self.loging_button = self.page.locator("//button[contains(text(),' SIGN IN ')]")

    # def naviage(self):
    #     self.page.goto(f"https://{self.serverip}")

    def enter_username(self,username):
        self.username_input.fill(username)
        self.log.info(f"entered username : {username}")

    def enter_password(self,password):
        self.password_input.fill(password)
        self.log.info(f"entered password : {password}")

    def click_login(self):
        self.loging_button.click()
        self.log.info(f"clicked on signin button")

    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()