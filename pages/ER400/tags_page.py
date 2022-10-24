import time
from util.logger import get_logger

class TagsPage:
    def __init__(self,page):
        self.page = page
        self.log = get_logger()
        self.tag_table = self.page.locator("//table/tbody")
        self.delete_tag_button = self.page.locator("//thead/tr[1]/th[6]/i[1]")

    def click_add_tag(self):
        self.page.locator("//button[text()=' Add Tag ']").click()
        self.log.info("clicked on add tag button")

    def enter_tag_name(self,name=None):
        self.page.locator("//textarea[@name='value']").fill(name)
        self.log.info(f"entered tag name : {name}")

    def click_add(self):
        self.page.locator("//button[text()='Add']").click()
        self.log.info("clicked on add button")

    def enter_search(self,name=None):
        self.page.locator("//input[@name='search']").fill(name)
        self.page.locator("//input[@name='search']").press('Enter')
        self.log.info(f"entered tag name for search : {name}")
        time.sleep(5)

    def is_tag_exist(self,name=None):
        flag = False
        rows = self.tag_table.locator("//tr").count()
        for row in range(rows-1):
            tag_name = self.tag_table.locator("//tr").nth(row).locator("//td[2]").text_content()
            if name == tag_name:
                flag=True
                break
            else:
                pass
        if flag:
            self.log.info(f"tag:{name} exists")
            return True
        else:
            self.log.info(f"tag : {name} does not exist")
            return False

    def assign_tag_to_host(self,host_name=None):
        self.page.locator("//button[contains(text(),'Assign To Host')]").click()
        self.log.info("clicked on assign host button")
        self.page.locator("//angular2-multiselect[@formcontrolname='hostName']").click()
        self.page.locator(f"//label[contains(text(),'{host_name}')]").click()
        self.page.locator("//angular2-multiselect[@formcontrolname='hostName']").click()
        self.log.info(f"selected host : {host_name}")
        self.page.locator("//button[text()='Assign']").click()
        self.log.info("clicked on assign button")

    def open_tag_info(self,name=None):
        flag = False
        rows = self.tag_table.locator("//tr").count()
        for row in range(rows - 1):
            tag_name = self.tag_table.locator("//tr").nth(row).locator("//td[2]").text_content()
            if name == tag_name:
                self.tag_table.locator("//tr").nth(row).locator("//td[2]/span/a").click()
                flag=True
                break
            else:
                pass
        if flag:
            self.log.info(f"clicked on tag {name} ")
        else:
            self.log.info(f"tag : {name} does not exist")


    def delete_tags(self,tags=[]):
        rows = self.tag_table.locator("//tr").count()
        for row in range(rows - 1):
            tag_name = self.tag_table.locator("//tr").nth(row).locator("//td[2]").text_content()
            if tag_name in tags:
                self.tag_table.locator("//tr").nth(row).locator("//td[1]/input").check()
                tags.remove(tag_name)
            else:
                pass
            if len(tags) == 0:
                break
        self.delete_tag_button.click()
        self.log.info("clicked on delete tag")
        self.page.locator("//button[contains(text(),'OK')]").click()
        self.log.info("clicked on delete OK button")
        time.sleep(5)




