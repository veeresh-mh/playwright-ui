import pytest
from util.logger import *
from pages.ER400.login_page import LoginPage
from pages.ER400.dashboard_page import DashboardPage
from pages.ER400.response_actions_page import ResponseActionsPage
from pages.ER400.response_file_page import ResponseFilePage
log = get_logger()


@pytest.fixture
def page(before_each_after_each,data):
    page = before_each_after_each
    login = LoginPage(page)
    login.login(data['username'],data['password'])
    return page

def test_delete_non_existing_file(page,data):
    dashboard = DashboardPage(page)
    response = ResponseActionsPage(page)
    file = ResponseFilePage(page)
    dashboard.click_response_action()
    response.click_create_new_response_action()
    response.click_file_tab()
    response.select_host(host=data['windowshostname'])
    file.enter_file_name(name='non-exist-file.txt')
    file.click_send_file_action()
    result = response.get_latest_response_info()
    assert result['action'] == 'delete'
    assert result['target'] == ' file '
    assert result['executed'] == '1/1'
    assert result['created_at'] != None
    assert result['created_by'] == ' admin '
    response.click_response_view()
    result = response.get_response_view_info()
    assert result['hostname'] == data['windowshostname']
    assert result['message'] == 'FILE_NOT_DELETED'
    assert result['status'] == 'Failure'
    assert result['created_at'] != None
    assert result['updated_at'] != None

def test_delete_file_with_invalid_hash(page,data):
    dashboard = DashboardPage(page)
    response = ResponseActionsPage(page)
    file = ResponseFilePage(page)
    dashboard.click_response_action()
    response.click_create_new_response_action()
    response.click_file_tab()
    response.select_host(host=data['windowshostname'])
    file.enter_file_name(name="C:\\Users\\Administrator\\Downloads\\ab_test.py")
    file.enter_file_hash(hash="inavalidhashsdasasd")
    file.click_send_file_action()
    result = response.get_latest_response_info()
    assert result['action'] == 'delete'
    assert result['target'] == ' file '
    assert result['executed'] == '1/1'
    assert result['created_at'] != None
    assert result['created_by'] == ' admin '
    response.click_response_view()
    result = response.get_response_view_info()
    assert result['hostname'] == data['windowshostname']
    assert result['message'] == 'HASH_NOT_MATCHED'
    assert result['status'] == 'Failure'
    assert result['created_at'] != None
    assert result['updated_at'] != None

def test_delete_valid_file(page,data):
    dashboard = DashboardPage(page)
    response = ResponseActionsPage(page)
    file = ResponseFilePage(page)
    dashboard.click_response_action()
    response.click_create_new_response_action()
    response.click_file_tab()
    response.select_host(host=data['windowshostname'])
    file.enter_file_name(name="C:\\Users\\Administrator\\Downloads\\ab_test.py")
    file.click_send_file_action()
    result = response.get_latest_response_info()
    assert result['action'] == 'delete'
    assert result['target'] == ' file '
    assert result['executed'] == '1/1'
    assert result['created_at'] != None
    assert result['created_by'] == ' admin '
    response.click_response_view()
    result = response.get_response_view_info()
    assert result['hostname'] == data['windowshostname']
    assert result['message'] == 'FILE_DELETED'
    assert result['status'] == 'Success'
    assert result['created_at'] != None
    assert result['updated_at'] != None