from util.logger import get_logger
from playwright.sync_api import expect

class RulesPage:
    def __init__(self,page):
        self.page = page
        self.log = get_logger()

    def click_create_rule(self):
        self.page.locator("//button[text()='Create Rule']").click()
        self.log.info("clicked on create rule button")

    def enter_rule_name(self,name):
        self.page.locator("//input[@id='name']").fill(name)
        self.log.info(f"entered rule name : {name}")

    def enter_description(self,desc):
        self.page.locator("//textarea[@name='description']").fill(desc)
        self.log.info(f"entered description : {desc}")

    def select_alerter(self,alerter):
        self.page.locator("//angular2-multiselect[@formcontrolname='alerters']").click()
        self.page.locator(f"//label[text()='{alerter}']").click()
        self.log.info(f"selected alerter : {alerter}")

    def create_condition(self,filter=None,operator=None,value=None):
        self.page.locator("//select[@name='query-builder_rule_0_filter']").select_option(label=filter)
        self.log.info(f"selected filter : {filter}")

        self.page.locator("//select[@name='query-builder_rule_0_operator']").select_option(label=operator)
        self.log.info(f"selected operator : {operator}")

        self.page.locator("//input[@name='query-builder_rule_0_value_0']").fill(value)
        self.log.info(f"value is : {value}")

    def select_status(self,status=None):
        self.page.locator("//select[@id='status']").select_option(label=status)
        self.log.info(f"selected status : {status}")

    def select_severity(self,severity=None):
        self.page.locator("//select[@id='severity']").select_option(label=severity)
        self.log.info(f"selected severity : {severity}")

    def select_platform(self,platform=None):
        self.page.locator("//select[@id='platform']").select_option(label=platform)
        self.log.info(f"selected platform : {platform}")

    def select_rule_type(self,type=None):
        if type == "DEFAULT":
            #self.page.locator("//input[@id='rule_type-1']").check()
            self.page.locator("//label[contains(text(),'Default')]").click()
            expect(self.page.locator("//input[@id='rule_type-1']")).to_be_checked()
            self.log.info("checked DEFAULT rule type")
        elif type == "MITRE":
            #self.page.locator("//input[@id='rule_type-0']").check()
            self.page.locator("//label[contains(text(),'MITRE')]").click()
            expect(self.page.locator("//input[@id='rule_type-0']")).to_be_checked()
            self.log.info("checked MITRE rule type")

    def enter_technique_id(self,id=None):
        self.page.locator("//input[@name='technique_id']").fill(id)
        self.log.info(f"entered technique id : {id}")

    def select_tactics(self,tactics=None):
        self.page.locator("//angular2-multiselect[@formcontrolname='tactics']").click()
        self.page.locator(f"//label[contains(text(),'{tactics}')]").click()
        self.log.info(f"selected tactics : {tactics}")

    def click_add_rule(self):
        self.page.locator("//button[text()='Add Rule']").click()
        self.log.info("clicked on add rule button")

    def select_rule_status(self,status=None):
        self.page.locator('.dropdown-btn > .ng-star-inserted').click()
        if status == 'Active':
            self.page.locator('.item2 > :nth-child(1) > div').click()
            self.log.info("selected active rules")
        elif status == 'Inactive':
            self.page.locator('.item2 > :nth-child(2) > div').click()
            self.log.info("selected inactive rules")

    def search_rule(self,name):
        self.page.locator("//input[@id='customsearch']").fill(name)
        self.page.locator("//search/i").click(force=True)
        self.log.info(f"searching for rule : {name}")

    def click_update(self):
        self.page.locator("//button[text()='Update']").click()
        self.log.info("clicked on update button")

    def open_rule(self,name=None):
        flag = False
        self.search_rule(name)
        table = self.page.locator("//table[@id='ruletable']")
        total_rows = table.locator("//tbody/tr").count()
        for row in range(total_rows-1):
            rule_name = table.locator("//tbody/tr").nth(row).locator("//td[2]/a").text_content()
            if rule_name == f" {name}":
                self.page.locator("//table[@id='ruletable']/tbody/tr").nth(row).locator("//td[6]/div/a/i").click()
                self.log.info("clicked on menu button")
                self.page.locator("//table[@id='ruletable']/tbody/tr").nth(row).locator("//td[6]/div/div/a[1]").click()
                flag = True
                break
            else:
                pass
        if flag:
            self.log.info("rule found and clicked on open")
            return True
        else:
            self.log.info("could not find rule")
            return False

    def edit_rule(self,name=None):
        flag = False
        self.search_rule(name)
        table = self.page.locator("//table[@id='ruletable']")
        total_rows = table.locator("//tbody/tr").count()
        for row in range(total_rows-1):
            rule_name = table.locator("//tbody/tr").nth(row).locator("//td[2]/a").text_content()
            if rule_name == f" {name}":
                self.page.locator("//table[@id='ruletable']/tbody/tr").nth(row).locator("//td[6]/div/a/i").click()
                self.log.info("clicked on menu button")
                self.page.locator("//table[@id='ruletable']/tbody/tr").nth(row).locator("//td[6]/div/div/a[3]").click()
                flag = True
                break
            else:
                pass
        if flag:
            self.log.info("rule found and clicked on edit")
            return True
        else:
            self.log.info("could not find rule")
            return False
