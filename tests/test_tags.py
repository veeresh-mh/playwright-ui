import random
import pytest
from util.logger import *
from pages.ER400.login_page import LoginPage
from pages.ER400.dashboard_page import DashboardPage
from pages.ER400.tags_page import TagsPage
from pages.ER400.hosts_page import HostsPage
from playwright.sync_api import expect
log = get_logger()

tag_name = f"auto-ui-tag-{random.randint(1,999)}"

@pytest.fixture
def page(before_each_after_each,data):
    page = before_each_after_each
    login = LoginPage(page)
    login.login(data['username'],data['password'])
    return page

@pytest.mark.dependency()
def test_tag_creation(page,data):
    dashboard = DashboardPage(page)
    tags = TagsPage(page)
    dashboard.click_tags()
    tags.click_add_tag()
    tags.enter_tag_name(name=tag_name)
    tags.click_add()
    tags.enter_search(name=tag_name)
    tags.is_tag_exist(name=tag_name)

@pytest.mark.dependency(depends=["test_tag_creation"])
def test_assign_tag_to_host(page,data):
    dashboard = DashboardPage(page)
    tags = TagsPage(page)
    dashboard.click_tags()
    hosts = HostsPage(page)
    tags.enter_search(name=tag_name)
    tags.open_tag_info(name=tag_name)
    expect(page.locator("//h4[contains(text(),'Hosts Tagged')]/strong")).to_contain_text(tag_name)
    tags.assign_tag_to_host(host_name=data['windowshostname'])
    expect(page.locator(f"//a[contains(text(),'{data['windowshostname']}')]")).to_be_visible()
    dashboard.click_hosts()
    tags_list = hosts.get_host_tags(host_name=data['windowshostname'])
    assert tag_name in tags_list

@pytest.mark.dependency(depends=["test_tag_creation"])
def test_delete_tag(page,data):
    dashboard = DashboardPage(page)
    tags = TagsPage(page)
    dashboard.click_tags()
    tags.delete_tags(tags=[tag_name])
    assert not tags.is_tag_exist(name=tag_name)