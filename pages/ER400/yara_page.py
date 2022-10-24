import time
from util.logger import get_logger

class YaraPage:
    def __init__(self,page):
        self.page = page
        self.log = get_logger()

    def click_add_yara_file(self):
        self.page.locator("//button/span[text()='Add YARA File']").click()
        self.log.info("clicked on ad yara file button")

    def chose_yara_file(self,file=None):
        self.page.locator("//input[@id='customFile']").set_input_files(f"./yara/{file}")
        self.log.info(f"chosen file : {file}")


