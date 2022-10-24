import pytest
from playwright.sync_api import expect
from util.logger import *
from pages.ER400.login_page import LoginPage
from pages.ER400.dashboard_page import DashboardPage
from pages.ER400.response_actions_page import ResponseActionsPage
from pages.ER400.response_custom_action import CustomResponseAction
log = get_logger()

@pytest.fixture
def page(before_each_after_each,data):
    page = before_each_after_each
    login = LoginPage(page)
    login.login(data['username'],data['password'])
    return page

def test_custom_batch_action(page,data):
    dashboard = DashboardPage(page)
    response = ResponseActionsPage(page)
    customaction = CustomResponseAction(page)
    dashboard.click_response_action()
    response.click_create_new_response_action()
    response.click_custom_action_tab()
    response.select_host(host=data['windowshostname'])
    customaction.enter_script_name(name="batch-script")
    customaction.enter_script_content(content="tasklist | findstr plgx")
    customaction.select_script_type(type='batch')
    customaction.click_send_custom_action()
    result = response.get_latest_response_info()
    assert result['action'] == 'Batch'
    assert result['target'] == ' script/batch-script '
    assert result['executed'] == '1/1'
    assert result['created_at'] != None
    assert result['created_by'] == ' admin '
    response.click_response_view()
    result = response.get_response_view_info()
    assert result['hostname'] == data['windowshostname']
    assert result['message'] == 'SCRIPT_EXECUTION_SUCCESSFULL'
    assert result['status'] == 'Success'
    assert result['created_at'] != None
    assert result['updated_at'] != None
    response_data = response.get_response_data()
    assert "plgx_agent.exe" in response_data and "plgx_osqueryd.exe" in response_data



