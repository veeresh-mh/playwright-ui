import random
import pytest
from util.logger import *
from pages.ER400.livequery_page import LivequeryPage
from pages.ER400.login_page import LoginPage
from pages.ER400.dashboard_page import DashboardPage
from playwright.sync_api import expect
log = get_logger()

@pytest.fixture
def page(before_each_after_each,data):
    page = before_each_after_each
    login = LoginPage(page)
    login.login(data['username'],data['password'])
    return page

def test_livequery_with_hostname(page,data):
    dashboard = DashboardPage(page)
    livequery = LivequeryPage(page)
    dashboard.click_er_rules()
    dashboard.click_livequery()
    livequery.select_hostname(host=data['windowshostname'])
    livequery.enter_livequery(query="select * from system_info")
    livequery.click_run_query()
    expect(page.locator("//div[contains(text(),'100.00% (1 / 1)')]")).to_be_visible()
    livequery.click_status_tab()
    livequery.verify_livquery_status()
    livequery.click_Results_tab()
    assert len(livequery.get_livequery_results()) != 0

def test_livequery_with_osname(page,data):
    dashboard = DashboardPage(page)
    livequery = LivequeryPage(page)
    dashboard.click_er_rules()
    dashboard.click_livequery()
    livequery.select_operating_system(os='Windows')
    livequery.enter_livequery(query="select * from system_info")
    livequery.click_run_query()
    expect(page.locator("//div[contains(text(),'100.00% (1 / 1)')]")).to_be_visible()
    livequery.click_status_tab()
    livequery.verify_livquery_status()
    livequery.click_Results_tab()
    assert len(livequery.get_livequery_results()) != 0

def test_livequery_with_tags(page,data):
    dashboard = DashboardPage(page)
    livequery = LivequeryPage(page)
    dashboard.click_er_rules()
    dashboard.click_livequery()
    livequery.select_tagname(tag='auto-host')
    livequery.enter_livequery(query="select * from system_info")
    livequery.click_run_query()
    expect(page.locator("//div[contains(text(),'100.00% (1 / 1)')]")).to_be_visible()
    livequery.click_status_tab()
    livequery.verify_livquery_status()