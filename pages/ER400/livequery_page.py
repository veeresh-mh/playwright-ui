import time

from util.logger import *
from playwright.sync_api import expect

class LivequeryPage:
    def __init__(self,page):
        self.page = page
        self.log = get_logger()

    def enter_livequery(self,query=None):
        self.page.locator("//ace-editor//textarea").fill(query)
        self.log.info(f"entered query : {query}")

    def select_hostname(self,host=None):
        self.page.locator("//span[contains(text(),'Select by Host')]").click()
        self.page.locator("//input[@placeholder='Search host here..']").fill(host)
        self.page.locator(f"//label[contains(text(),'{host}')]").click()
        self.log.info(f"selected host : {host}")
        time.sleep(3)

    def select_operating_system(self,os=None):
        self.page.locator("//span[contains(text(),'Select by Operating System')]").click()
        self.page.locator("//input[@placeholder='Search OS Name here..']").fill(os)
        self.page.locator(f"//label[contains(text(),'{os}')]").click()
        self.log.info(f"selected os : {os}")

    def select_tagname(self,tag=None):
        self.page.locator("//span[contains(text(),'Select by Tags')]").click()
        self.page.locator("//input[@placeholder='Search tag here..']").fill(tag)
        self.page.locator(f"//label[contains(text(),'{tag}')]").click()
        self.log.info(f"selected tag name : {tag}")

    def click_run_query(self):
        self.page.locator("//button[text()='Run Query']").click()
        self.log.info("clicked on run query")

    def verify_livquery_status(self):
        table = self.page.locator("//table[@class='table table-striped- table-bordered table-checkable']")
        total_rows = table.locator("//tbody/tr").count()
        for row in range(total_rows):
            expect(table.locator("//tbody/tr").nth(row).locator("//td[1]")).not_to_be_empty()
            expect(table.locator("//tbody/tr").nth(row).locator("//td[2]")).to_contain_text("Success")

    def click_status_tab(self):
        self.page.locator("//a[contains(text(),'Status')]").click()
        self.log.info("clicked on status tab")

    def click_Results_tab(self):
        self.page.locator("//a[contains(text(),'Results')]").click()
        self.log.info("clicked on result tab")

    def get_livequery_results(self):
        table = self.page.locator("//table[@id='live_query_table']")
        total_rows = table.locator("//tbody/tr").count()
        total_cols = table.locator("//thead/tr[1]/th").count()
        results = {}
        hostname = None
        for row in range(total_rows):
            if table.locator("//tbody/tr").nth(row).locator("//td").count() == 1:
                host_name = table.locator("//tbody/tr").nth(row).locator("//td[1]").text_content()
            else:
                row_data =[]
                col_data = {}
                for col in range(total_cols):
                    col_data[table.locator("//thead/tr[1]/th").nth(col).text_content()] = table.locator("//tbody/tr").nth(row).locator("//td").nth(col).text_content()
                row_data.append(col_data)
                results[host_name]=row_data
        self.log.info(results)
        return results
