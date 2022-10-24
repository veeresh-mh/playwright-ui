from playwright.sync_api import expect

from util.logger import get_logger

class ResponseActionsPage:
    def __init__(self,page):
        self.page = page
        self.log = get_logger()
        self.table = self.page.locator("//table/tbody")

    def click_create_new_response_action(self):
        self.page.locator("//button[text()='Create New Response Action']").click()
        self.log.info("clicked on create action button")

    def select_host(self,host=None):
        self.page.locator("//span[contains(text(),'Select Host(s)')]").click()
        self.page.locator("//input[@placeholder='Search Hosts here..']").fill(host)
        self.page.locator(f"//label[contains(text(),'{host}')]").click()
        self.log.info(f"selected host : {host}")

    def click_file_tab(self):
        self.page.locator("//a[contains(text(),'File')]").click()
        self.log.info("clicked on file tab")

    def click_process_tab(self):
        self.page.locator("//a[contains(text(),'Process')]").click()
        self.log.info("clicked on process tab")

    def click_network_tab(self):
        self.page.locator("//a[contains(text(),'Network')]").click()
        self.log.info("clicked on network tab")

    def click_custom_action_tab(self):
        self.page.locator("//a[contains(text(),'Custom Action')]").click()
        self.log.info("clicked on custom action tab")

    def get_latest_response_info(self):
        result = {}
        result['action'] = self.table.locator("//tr[1]/td[2]").text_content()
        result['target'] = self.table.locator("//tr[1]/td[3]").text_content()
        result['executed'] = self.table.locator("//tr[1]/td[5]").text_content()
        result['created_at'] = self.table.locator("//tr[1]/td[6]").text_content()
        result['created_by'] = self.table.locator("//tr[1]/td[7]").text_content()
        self.log.info(f"latest response info : {result}")
        return result

    def click_response_view(self):
        self.table.locator("//tr[1]/td[8]/div/a/i").click()
        self.log.info("clicked on response view")

    def get_response_view_info(self):
        result = {}
        result['hostname'] = self.table.locator("//tr[1]/td[1]").text_content()
        result['message'] = self.table.locator("//tr[1]/td[2]").text_content()
        result['status'] = self.table.locator("//tr[1]/td[4]").text_content()
        result['created_at'] = self.table.locator("//tr[1]/td[5]").text_content()
        result['updated_at'] = self.table.locator("//tr[1]/td[6]").text_content()
        self.log.info(f"response view info : {result}")
        return result

    def get_response_data(self):
        expect(self.table.locator("//tr[1]/td[3]/i")).to_be_enabled()
        self.table.locator("//tr[1]/td[3]/i").click()
        self.log.info("view button is enabled and clicked")
        response_data = self.page.locator("//pre").text_content()
        self.log.info(f"response data : {response_data}")
        self.page.locator("//body/app-root[1]/app-global[1]/div[1]/app-view-openc2[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/button[1]").click()
        self.log.info("clicked on response data close")
        return response_data


