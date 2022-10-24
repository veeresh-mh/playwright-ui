import json
import pytest
from util.logger import *
from screeninfo import get_monitors
from playwright.sync_api import Playwright,sync_playwright

width = get_monitors()[0].width
height = get_monitors()[0].height

log = get_logger()

@pytest.fixture
def data():
    with open('test_data.json') as file:
        data = json.load(file)
    return data

def teardown(page):
    page.locator("//span[contains(text(),'Logout')]").click()
    log.info("clicked on logout")

@pytest.fixture(scope="function",autouse=True)
def before_each_after_each(data,playwright: Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=500,timeout=10000)
    log.info("browser launched")
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = browser.new_page(ignore_https_errors=True)
    page.set_viewport_size({"width":width,"height":height})
    page.goto(f"https://{data['server']}")
    log.info(f"accessing server : https://{data['server']}")
    yield page
    teardown(page)
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()





