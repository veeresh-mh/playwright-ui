from util.logger import *
from playwright.sync_api import expect

class HostDetailsPage:
    def __init__(self,page):
        self.page = page
        self.log = get_logger()

    def click_details(self):
        self.page.locator("//a[contains(text(),'Details')]").click()
        self.log.info("clicked on details tab")

    def click_network_info(self):
        self.page.locator("//a[contains(text(),'Network Info')]").click()
        self.log.info("clicked on netrwork info tab")

    def click_tags_tab(self):
        self.page.locator("//a[contains(text(),'Tags')]").click()
        self.log.info("clicked on tags tab")

    def click_status_log_tab(self):
        self.page.locator("//a[contains(text(),'Status Log')]").click()
        self.log.info("clicked on status log tab")

    def click_security_center_tab(self):
        self.page.locator("//a[contains(text(),'Security Center')]").click()
        self.log.info("clicked on security center tab")

    def click_live_terminal_tab(self):
        self.page.locator("//a[contains(text(),'Live Terminal')]").click()
        self.log.info("clicked on live twrminal tab")

    def click_recent_activity_tab(self):
        self.page.locator("//a[contains(text(),'Recent Activity')]").click()
        self.log.info("clicked on recent activity tab")

