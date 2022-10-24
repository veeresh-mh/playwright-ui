import pytest
from playwright.sync_api import expect

from util.logger import *
from pages.ER400.login_page import LoginPage
from pages.ER400.dashboard_page import DashboardPage
from pages.ER400.response_actions_page import ResponseActionsPage
from pages.ER400.response_process_page import ResponseProcessPage
log = get_logger()

@pytest.fixture
def page(before_each_after_each,data):
    page = before_each_after_each
    login = LoginPage(page)
    login.login(data['username'],data['password'])
    return page

def test_stop_invalid_process(page,data):
    dashboard = DashboardPage(page)
    response = ResponseActionsPage(page)
    process = ResponseProcessPage(page)
    dashboard.click_response_action()
    response.click_create_new_response_action()
    response.click_process_tab()
    response.select_host(host=data['windowshostname'])
    process.enter_process_name(name="invalid file name")
    process.enter_process_id(id=12112)
    process.click_send_process_action()
    result = response.get_latest_response_info()
    assert result['action'] == 'stop'
    assert result['target'] == ' process '
    assert result['executed'] == '1/1'
    assert result['created_at'] != None
    assert result['created_by'] == ' admin '
    response.click_response_view()
    result = response.get_response_view_info()
    assert result['hostname'] == data['windowshostname']
    assert result['message'] == 'PROC_OPEN_FAILED' or result['message'] == 'PROC_NAME_NO_MATCH'
    assert result['status'] == 'Failure'
    assert result['created_at'] != None
    assert result['updated_at'] != None

def test_stop_valid_process_with_invalid_id(page,data):
    dashboard = DashboardPage(page)
    response = ResponseActionsPage(page)
    process = ResponseProcessPage(page)
    dashboard.click_response_action()
    response.click_create_new_response_action()
    response.click_process_tab()
    response.select_host(host=data['windowshostname'])
    process.enter_process_name(name="notepad.exe")
    process.enter_process_id(id=12112)
    process.click_send_process_action()
    result = response.get_latest_response_info()
    assert result['action'] == 'stop'
    assert result['target'] == ' process '
    assert result['executed'] == '1/1'
    assert result['created_at'] != None
    assert result['created_by'] == ' admin '
    response.click_response_view()
    result = response.get_response_view_info()
    assert result['hostname'] == data['windowshostname']
    assert result['message'] == 'PROC_OPEN_FAILED' or result['message'] == 'PROC_NAME_NO_MATCH'
    assert result['status'] == 'Failure'
    assert result['created_at'] != None
    assert result['updated_at'] != None

def test_stop_process_without_id(page,data):
    dashboard = DashboardPage(page)
    response = ResponseActionsPage(page)
    process = ResponseProcessPage(page)
    dashboard.click_response_action()
    response.click_create_new_response_action()
    response.click_process_tab()
    response.select_host(host=data['windowshostname'])
    process.enter_process_name(name="notepad.exe")
    process.click_send_process_action()
    expect(page.locator("//div[contains(text(),'Error On Process Id Field')]")).to_be_visible()
