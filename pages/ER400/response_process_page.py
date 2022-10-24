from util.logger import get_logger

class ResponseProcessPage:
    def __init__(self,page):
        self.page = page
        self.log = get_logger()

    def enter_process_name(self,name=None):
        self.page.locator("//input[@id='process_name']").fill(name)
        self.log.info(f"entered process name : {name}")

    def enter_process_id(self,id=None):
        self.page.locator("//input[@id='pid']").fill(str(id))
        self.log.info(f"entered pid : {id}")

    def click_send_process_action(self):
        self.page.locator("//*[@id='action_process']/form/div/div/div/div/div[6]/appbutton/button").click()
        self.log.info("clicked process send button")