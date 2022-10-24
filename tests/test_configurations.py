import random
import time
import pytest
from util.logger import *
from pages.ER400.configurations_page import ConfigurationsPage
from pages.ER400.login_page import LoginPage
from pages.ER400.dashboard_page import DashboardPage
from playwright.sync_api import expect
log = get_logger()

windwos_config = f"ui-win-{random.randint(1,999)}"
linux_config = f"ui-linux-{random.randint(1,999)}"
darwin_config = f"ui-darwin-{random.randint(1,999)}"

@pytest.fixture
def page(before_each_after_each,data):
    page = before_each_after_each
    login = LoginPage(page)
    login.login(data['username'],data['password'])
    return page

def test_windows_config_creation(page,data):
    dashboard = DashboardPage(page)
    config = ConfigurationsPage(page)
    dashboard.click_configurations()
    config.click_windows_tab()
    config.click_create_config()
    config.enter_config_name(name=windwos_config)
    config.enter_config_description(desc="some description")
    config.select_config(config_name='Deep')
    config.enter_host_name_pattern(pattern="*EC2*")
    config.enter_os_name_pattern(pattern="*windows*")
    config.click_create()
    config.click_windows_tab()
    config.is_config_created(config_name=windwos_config)

def test_linux_config_creation(page,data):
    dashboard = DashboardPage(page)
    config = ConfigurationsPage(page)
    dashboard.click_configurations()
    config.click_linux_tab()
    config.click_create_config()
    config.enter_config_name(name=linux_config)
    config.enter_config_description(desc="some description")
    config.select_config(config_name='Default')
    config.enter_host_name_pattern(pattern="*ip*")
    config.enter_os_name_pattern(pattern="*ubuntu*")
    config.click_create()
    config.click_linux_tab()
    config.is_config_created(config_name=linux_config)

def test_darwin_config_creation(page,data):
    dashboard = DashboardPage(page)
    config = ConfigurationsPage(page)
    dashboard.click_configurations()
    config.click_darwin_tab()
    config.click_create_config()
    config.enter_config_name(name=darwin_config)
    config.enter_config_description(desc="some description")
    config.select_config(config_name='Default')
    config.enter_host_name_pattern(pattern="*ip*")
    config.enter_os_name_pattern(pattern="*macOs*")
    config.click_create()
    config.click_darwin_tab()
    config.is_config_created(config_name=darwin_config)