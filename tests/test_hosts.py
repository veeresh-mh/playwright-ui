import time
import pytest
from util.logger import *
from pages.ER400.hosts_page import HostsPage
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

def test_listing_only_windows_hosts(data,page):
    dashboard = DashboardPage(page)
    hosts = HostsPage(page)
    dashboard.click_hosts()
    hosts.select_platform('Windows')
    page.wait_for_load_state()
    time.sleep(5)
    table = page.locator("//table[@id='host_table']")
    rows  = table.locator("//tbody/tr").count()
    for row in range(rows-1):
        expect(table.locator("//tbody/tr").nth(row).locator('//td[5]')).to_contain_text('Windows')

def test_listing_only_linux_hosts(data,page):
    dashboard = DashboardPage(page)
    hosts = HostsPage(page)
    dashboard.click_hosts()
    hosts.select_platform('Linux')
    page.wait_for_load_state()
    time.sleep(5)
    rows = page.locator("//table[@id='host_table']/tbody/tr").count()
    for row in range(rows-1):
        expect(page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator('//td[5]')).to_contain_text('Ubuntu')

# def test_listing_only_darwin_hosts(data,page):
#     dashboard = DashboardPage(page)
#     hosts = HostsPage(page)
#     dashboard.click_hosts()
#     hosts.selectPlatform('Darwin')
#     page.wait_for_load_state()
#     time.sleep(5)
#     rows = page.locator("//table[@id='host_table']/tbody/tr").count()
#     for row in range(rows-1):
#         expect(page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator('//td[5]')).to_contain_text('macOS')

def test_list_any_host_status(data,page):
    dashboard = DashboardPage(page)
    hosts = HostsPage(page)
    dashboard.click_hosts()
    hosts.select_host_status('any')
    page.wait_for_load_state()
    time.sleep(5)
    rows = page.locator("//table[@id='host_table']/tbody/tr").count()
    for row in range(rows-1):
        host = page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator('//td[2]/a').text_content()
        status = page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator('//td[3]/i').get_attribute('title')
        log.info(f"{host} : {status}")
        assert 'Online' in status  or  'Offline' in status or 'Degraded' in status

def test_listing_only_Online_Hosts(data,page):
    dashboard = DashboardPage(page)
    hosts = HostsPage(page)
    dashboard.click_hosts()
    hosts.select_host_status('Online')
    page.wait_for_load_state()
    time.sleep(5)
    rows = page.locator("//table[@id='host_table']/tbody/tr").count()
    for row in range(rows-1):
        host = page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator('//td[2]/a').text_content()
        status = page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator('//td[3]/i').get_attribute('title')
        log.info(f"{host} : {status}")
        assert 'Online' in status or 'Online' in status or 'Degraded' in status

def test_listing_only_Offline_Hosts(data,page):
    dashboard = DashboardPage(page)
    hosts = HostsPage(page)
    dashboard.click_hosts()
    hosts.select_host_status('Offline')
    page.wait_for_load_state()
    time.sleep(5)
    rows = page.locator("//table[@id='host_table']/tbody/tr").count()
    for row in range(rows-1):
        host = page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator('//td[2]/a').text_content()
        status = page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator('//td[3]/i').get_attribute('title')
        log.info(f"{host} : {status}")
        expect(page.locator("//table[@id='host_table']/tbody/tr").nth(row).locator('//td[3]/i')).to_have_attribute('title','Status Offline')

def test_host_information(data,page):
    dashboard = DashboardPage(page)
    hosts = HostsPage(page)
    dashboard.click_hosts()
    hosts.search_host(data['windowshostname'])
    hosts.open_host(data['windowshostname'])
    expect(page.locator(f"//label[contains(text(),'{data['windowshostname']}')]")).to_be_visible()

@pytest.mark.dependency()
def test_disable_host(data,page):
    dashboard = DashboardPage(page)
    hosts = HostsPage(page)
    dashboard.click_hosts()
    hosts.disable_host(data['windowshostname'])
    #valication yet to add , background issue

@pytest.mark.dependency(depends=["test_disable_host"])
def test_restore_host(data,page):
    dashboard = DashboardPage(page)
    hosts = HostsPage(page)
    dashboard.click_hosts()
    hosts.click_archived()
    hosts.restore_host(data['windowshostname'])
    hosts.click_active()
    assert hosts.is_host_exists(data['windowshostname'])
