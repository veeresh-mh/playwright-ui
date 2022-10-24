import time

from util.logger import *

class DashboardPage:
    def __init__(self,page):
        self.page = page
        self.log = get_logger()
        self.hosts_link = self.page.locator("//span[contains(text(),'Hosts')]")

    def click_hosts(self):
        self.hosts_link.click()
        self.log.info("clicked on hosts")
        time.sleep(5)

    def click_er_rules(self):
        self.page.locator("//a/span[text()='Rules']").click()
        self.page.locator("//a/span[text()='ER Rules']").click()
        self.log.info("clicked on er rules link")

    def click_configurations(self):
        self.page.locator("//span[contains(text(),'Host Configuration')]").click()
        self.page.locator("//span[text()='Configurations']").click()
        self.log.info("clicked on configurations link")
        time.sleep(5)

    def click_tags(self):
        self.page.locator("//span[contains(text(),'Host Configuration')]").click()
        self.page.locator("//span[text()='Tags']").click()
        self.log.info("clicked on tags link")
        time.sleep(5)

    def click_livequery(self):
        self.page.locator("//span[contains(text(),'Live Query')]").click()
        self.log.info("clicked on livequery link")

    def click_response_action(self):
        self.page.locator("//span[contains(text(),'Response Action')]").click()
        self.log.info("clicked on response action link")