from util.logger import get_logger

class CustomResponseAction:
    def __init__(self,page):
        self.page = page
        self.log = get_logger()

    def enter_script_name(self,name=None):
        self.page.locator("//input[@id='script_name']").fill(name)
        self.log.info(f"entered script name : {name}")

    def enter_script_content(self,content=None):
        self.page.locator("//textarea[@id='content']").fill(content)
        self.log.info(f"entered script content : {content}")

    def enter_params(self,params=None):
        self.page.locator("//input[@id='params']").fill(params)
        self.log.info(f"entred params : {params}")

    def select_script_type(self,type=None):
        if type == "batch":
            self.page.locator("//input[@name='script_type' and @value='1']").check()
            self.log.info("checked script type : batch")
        elif type == "powershell":
            self.page.locator("//input[@name='script_type' and @value='2']").check()
            self.log.info("checked script type : powershell")
        elif type == "shell":
            self.page.locator("//input[@name='script_type' and @value='4']").check()
            self.log.info("checked script type : shell")

    def click_send_custom_action(self):
        self.page.locator("//*[@id='cus_respose_form']/div/div/div/div/div[9]/appbutton/button").click()
        self.log.info("clicked on send custom action button")