import time
from util.logger import *

class HostsPage:
    def __init__(self,page):
        self.page = page
        self.log = get_logger()
        self.host_table = self.page.locator("//table[@id='host_table']/tbody")

    def select_platform(self,platform):
        self.page.locator("//single-select[@label='Platform: ']//child::span[text()='any']").click()
        self.page.locator(f"//div[contains(text(),'{platform}')]").click()
        self.log.info(f"selected platform : {platform}")

    def select_host_status(self,status):
        self.page.locator("//single-select[@label='Host Status: ']//child::span[text()='any']").click()
        self.page.locator(f"//single-select[@label='Host Status: ']/div/ng-multiselect-dropdown/div/div/ul/li/div[contains(text(),'{status}')]").click()
        self.log.info(f"selected host status:{status}")

    def search_host(self,hostname):
        self.page.locator("//input[@id='customsearch']").fill(hostname)
        self.page.locator("//input[@id='customsearch']").press('Enter')
        self.log.info(f"searching for : {hostname}")
        time.sleep(5)

    def open_host(self,hostname):
        rows = self.page.locator("//table[@id='host_table']/tbody/tr").count()
        self.log.info(rows)
        for row in range(rows - 1):
            host = self.page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator('//td[2]/a').text_content()
            self.log.info(row)
            if host == hostname:
                self.page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator('//td[8]/div/a').click()
                self.log.info("clicked on host menu")
                self.page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator("//td[8]/div/div/a[text()='Open']").click()
                self.log.info("clicked on host open option")
                self.page.locator("//a[@title='Open Host']/img").click()
                self.log.info("clicked on host extend info")
                break

    def disable_host(self,hostname):
        rows = self.page.locator("//table[@id='host_table']/tbody/tr").count()
        for row in range(rows - 1):
            host = self.page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator('//td[2]/a').text_content()
            if host == hostname:
                self.page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator('//td[8]/div/a').click()
                self.log.info("clicked on host menu")
                self.page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator("//td[8]/div/div/a[text()='Disable']").click()
                self.log.info("clicked on host disable otioon")
                self.page.locator("//button[contains(text(),'Yes, Remove it!')]").click()
                self.log.info("clicked on 'yes remove it' button")
                break

    def click_archived(self):
        self.page.locator("//a[@id='linux']").click()
        self.log.info("clicked on archived hosts tab")

    def click_active(self):
        self.page.locator("//a[@id='windows']").click()
        self.log.info("clicke on active hosts tab")

    def restore_host(self,hostname):
        status = False
        rows = self.page.locator("//table[@id='host_table']/tbody/tr").count()
        for row in range(rows - 1):
            host = self.page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator('//td[2]/a').text_content()
            if host == hostname:
                status = True
                self.page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator('//td[8]/div/a').click()
                self.log.info("clicked on host menu")
                self.page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator("//td[8]/div/div/a[text()='Restore Host']").click()
                self.log.info("clicked on host disable otioon")
                self.page.locator("//button[contains(text(),'Yes, Restore it!')]").click()
                self.log.info("clicked on 'yes remove it' button")
                break
        if status == False:
            self.log.debug(f"{host} does not exist")

    def is_host_exists(self,hostname):
        status = False
        rows = self.page.locator("//table[@id='host_table']/tbody/tr").count()
        for row in range(rows - 1):
            host = self.page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator('//td[2]/a').text_content()
            if host == hostname:
                status =  True
                self.log.info(f"{host} exists")
                break

        if status == False:
            self.log.error(f"{host} does not exist")
        return status

    def get_host_tags(self,host_name=None):
        '''
        get list of tags tagged to host
        :return:
        '''
        self.search_host(hostname=host_name)
        tags = self.host_table.locator("//tr/td[7]/tag-input/div/div/tag").count()
        tags_list = []
        for tag in range(tags):
            tags_list.append(self.host_table.locator("//tr/td[7]/tag-input/div/div/tag").nth(tag).text_content().strip())
        self.log.info(f"{host_name} has tags : {tags_list}")
        return tags_list
