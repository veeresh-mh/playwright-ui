import time

from util.logger import *
from playwright.sync_api import expect

class ConfigurationsPage:
    def __init__(self,page):
        self.page = page
        self.log = get_logger()

    def click_windows_tab(self):
        self.page.locator("//a[text()='Windows']").click()
        self.log.info("clicked on windows tab")

    def click_linux_tab(self):
        self.page.locator("//a[text()=' Linux']").click()
        self.log.info("clicked on linux tab")

    def click_darwin_tab(self):
        self.page.locator("//a[text()='Darwin']").click()
        self.log.info("clicked on linux tab")

    def click_create_config(self):
        self.page.locator("//button[text()='Create Config']").click()
        self.log.info("clicked on create config button")

    def click_on_config(self,config_name=None):
        self.page.locator(f"//a[contains(text(),'{config_name}')]").click()
        self.log.info(f"clicked on config : {config_name}")

    def enter_config_name(self,name=None):
        self.page.locator("//input[@id='Config_Name']").fill(name)
        self.log.info(f"entered config name : {name}")

    def enter_config_description(self,desc=None):
        self.page.locator("//input[@formcontrolname='Description']").fill(desc)
        self.log.info(f"entered config desc : {desc}")

    def select_config(self,config_name=None):
        self.page.locator("//div[@class='c-btn']//span[contains(text(),'Select Config')]").click()
        self.page.locator(f"//label[contains(text(),'{config_name}')]").click()
        self.log.info(f"selected config name : {config_name}")

    def enter_host_name_pattern(self,pattern=None):
        self.page.locator("//input[@formcontrolname='host_Name']").fill(pattern)
        self.log.info(f"entered host pattern : {pattern}")

    def enter_os_name_pattern(self,pattern=None):
        self.page.locator("//input[@formcontrolname='Os_Name']").fill(pattern)
        self.log.info(f"entered host pattern : {pattern}")

    def click_create(self):
        self.page.locator("//button[text()='Create']").click()
        self.page.locator("//button[contains(text(),'OK')]").click()
        self.log.info("clicked on create button")

    def is_config_created(self,config_name):
        expect(self.page.locator(f"//a[contains(text(),'{config_name}')]")).to_be_visible()
