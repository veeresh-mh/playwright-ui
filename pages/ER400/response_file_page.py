from util.logger import get_logger

class ResponseFilePage:
    def __init__(self,page):
        self.page = page
        self.log = get_logger()


    def enter_file_name(self,name=None):
        self.page.locator("//input[@id='file_name']").fill(name)
        self.log.info(f"entered file name : {name}")

    def enter_file_hash(self,hash=None):
        self.page.locator("//input[@id='hash']").fill(hash)
        self.log.info(f"entered hash : {hash}")

    def click_send_file_action(self):
        self.page.locator("//*[@id='action_file']/form/div/div/div/div/div[6]/appbutton/button").click()
        self.log.info("clicked on send file action button")

    