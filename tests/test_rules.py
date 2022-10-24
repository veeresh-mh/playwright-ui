import random
import pytest
from util.logger import *
from pages.ER400.rules_page import RulesPage
from pages.ER400.login_page import LoginPage
from pages.ER400.dashboard_page import DashboardPage
from playwright.sync_api import expect
log = get_logger()

default_rule_name = f"auto-default-rule-{random.randint(1,999)}"
mitre_rule_name = f"auto-mitre-rule-{random.randint(1,999)}"

@pytest.fixture
def page(before_each_after_each,data):
    page = before_each_after_each
    login = LoginPage(page)
    login.login(data['username'],data['password'])
    return page

def test_create_default_active_rule(page,data):
    dashboard = DashboardPage(page)
    rules = RulesPage(page)
    dashboard.click_er_rules()
    rules.click_create_rule()
    rules.enter_rule_name(default_rule_name)
    rules.enter_description(f"description of rule {default_rule_name}")
    rules.select_alerter('email')
    rules.create_condition(filter='Host Identifier',operator='contains',value='veer')
    rules.select_status(status='ACTIVE')
    rules.select_severity(severity='MEDIUM')
    rules.select_platform(platform='Windows')
    rules.select_rule_type(type="DEFAULT")
    rules.click_add_rule()
    rules.select_rule_status(status='Active')
    rules.search_rule(default_rule_name)
    assert rules.open_rule(name=default_rule_name)

def test_validate_default_active_rule_info(page,data):
    dashboard = DashboardPage(page)
    rules = RulesPage(page)
    dashboard.click_er_rules()
    rules.search_rule(default_rule_name)
    table = page.locator("//table[@id='ruletable']")
    flag = False
    for row in range(table.locator("//tbody/tr").count() - 1):
        rule = table.locator("//tbody/tr").nth(row).locator("//td[2]/a").text_content()
        if rule == f" {default_rule_name}":
            table.locator("//tbody/tr").nth(row).locator("//td[2]/a").click()
            expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[1]/td[1]")).to_have_text('Description')
            expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[1]/td[2]")).to_have_text(f"description of rule {default_rule_name}")

            expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[2]/td[1]")).to_contain_text('Alerters')
            expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[2]/td[2]")).to_contain_text('email')

            expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[3]/td[1]")).to_contain_text('Severity')
            expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[3]/td[2]")).to_contain_text('MEDIUM')

            expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[5]/td[1]")).to_contain_text('Type')
            expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[5]/td[2]")).to_contain_text('DEFAULT')
            break

def test_create_default_inactive_rule(page,data):
    dashboard = DashboardPage(page)
    rules = RulesPage(page)
    dashboard.click_er_rules()
    rules.click_create_rule()
    rules.enter_rule_name(f"{default_rule_name}-inactive")
    rules.enter_description(f"description of rule {default_rule_name}")
    rules.select_alerter('email')
    rules.create_condition(filter='Host Identifier',operator='contains',value='veer')
    rules.select_status(status='INACTIVE')
    rules.select_severity(severity='MEDIUM')
    rules.select_platform(platform='Windows')
    rules.select_rule_type(type="DEFAULT")
    rules.click_add_rule()
    rules.select_rule_status(status='Inactive')
    rules.search_rule(f"{default_rule_name}-inactive")
    table = page.locator("//table[@id='ruletable']")
    assert rules.open_rule(name=f"{default_rule_name}-inactive")

def test_validate_default_inactive_rule_info(page,data):
    dashboard = DashboardPage(page)
    rules = RulesPage(page)
    dashboard.click_er_rules()
    rules.select_rule_status(status='Inactive')
    rules.search_rule(f"{default_rule_name}-inactive")
    table = page.locator("//table[@id='ruletable']")
    flag = False
    for row in range(table.locator("//tbody/tr").count() - 1):
        rule = table.locator("//tbody/tr").nth(row).locator("//td[2]/a").text_content()
        if rule == f" {default_rule_name}-inactive":
            table.locator("//tbody/tr").nth(row).locator("//td[2]/a").click()
            expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[1]/td[1]")).to_have_text('Description')
            expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[1]/td[2]")).to_have_text(f"description of rule {default_rule_name}")

            expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[2]/td[1]")).to_contain_text('Alerters')
            expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[2]/td[2]")).to_contain_text('email')

            expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[3]/td[1]")).to_contain_text('Severity')
            expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[3]/td[2]")).to_contain_text('MEDIUM')

            expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[5]/td[1]")).to_contain_text('Type')
            expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[5]/td[2]")).to_contain_text('DEFAULT')
            break

def test_create_mitre_active_rule(page,data):
    dashboard = DashboardPage(page)
    rules = RulesPage(page)
    dashboard.click_er_rules()
    rules.click_create_rule()
    rules.enter_rule_name(mitre_rule_name)
    rules.enter_description(f"description of rule {mitre_rule_name}")
    rules.select_alerter('email')
    rules.create_condition(filter='Host Identifier',operator='contains',value='veer')
    rules.select_status(status='ACTIVE')
    rules.select_severity(severity='MEDIUM')
    rules.select_platform(platform='Windows')
    rules.select_rule_type(type="MITRE")
    rules.enter_technique_id(id='T1117')
    rules.select_tactics(tactics='Command and Control')
    rules.click_add_rule()
    rules.select_rule_status(status='Active')
    rules.search_rule(mitre_rule_name)
    table = page.locator("//table[@id='ruletable']")
    assert rules.open_rule(name=mitre_rule_name)

def test_updating_rule(page,data):
    dashboard = DashboardPage(page)
    rules = RulesPage(page)
    dashboard.click_er_rules()
    assert rules.edit_rule(name=default_rule_name)
    rules.enter_rule_name(name=f"{default_rule_name}-updated")
    rules.select_alerter('rsyslog')
    rules.select_severity(severity='HIGH')
    rules.select_status(status='INACTIVE')
    rules.click_update()
    rules.select_rule_status(status='Inactive')
    assert rules.open_rule(name=f"{default_rule_name}-updated")
    expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[2]/td[1]")).to_contain_text('Alerters')
    expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[2]/td[2]")).to_contain_text('email,rsyslog')

    expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[3]/td[1]")).to_contain_text('Severity')
    expect(page.locator("//appbutton/button/following::table[2]/tbody/tr[3]/td[2]")).to_contain_text('HIGH')


