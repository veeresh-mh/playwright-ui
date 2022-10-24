from pages.ER400.login_page import LoginPage
from playwright.sync_api import expect

def test_login_with_valid_credentails(before_each_after_each,data):
    page = before_each_after_each
    login = LoginPage(page)
    login.enter_username(data['username'])
    login.enter_password(data['password'])
    login.click_login()
    expect(page.locator("//h5[contains(text(),'Endpoint Response Dashboard')]")).to_be_visible()

def test_login_with_invalid_credentails(before_each_after_each,data):
    page = before_each_after_each
    login = LoginPage(page)
    login.enter_username(data['username'])
    login.enter_password("invalid")
    login.click_login()
    expect(page.locator("//span[contains(text(),'Incorrect Username or Password')]")).to_be_visible()