import pytest

from playwright.sync_api import expect

from config.settings import LOGIN_URL, DASHBOARD_URL
from pages.dashboard_page import DashboardPage
from test_data.login_data import (
    VALID_USERNAME,
    VALID_PASSWORD,
)

@pytest.mark.logout
def test_TC001_logout_successfully(login_page):
    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

    dashboard_page = DashboardPage(login_page.page)

    expect(dashboard_page.dashboard_heading).to_be_visible(
        timeout=15000
    )

    dashboard_page.logout()

    expect(login_page.page).to_have_url(
        LOGIN_URL,
        timeout=15000
    )

    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()

@pytest.mark.logout
def test_TC002_dashboard_access_after_logout(login_page):
    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

    dashboard_page = DashboardPage(login_page.page)

    expect(dashboard_page.dashboard_heading).to_be_visible(
        timeout=15000
    )

    dashboard_page.logout()

    expect(login_page.page).to_have_url(
        LOGIN_URL,
        timeout=15000
    )

    login_page.page.goto(
        DASHBOARD_URL,
        wait_until="domcontentloaded",
        timeout=60000
    )

    expect(login_page.page).to_have_url(
        LOGIN_URL,
        timeout=15000
    )

    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()

    expect(dashboard_page.dashboard_heading).not_to_be_visible()

@pytest.mark.logout
def test_TC003_browser_back_after_logout(login_page):
    page = login_page.page

    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

    dashboard_page = DashboardPage(page)

    expect(dashboard_page.dashboard_heading).to_be_visible(
        timeout=15000
    )

    dashboard_page.logout()

    expect(page).to_have_url(
        LOGIN_URL,
        timeout=15000
    )

    expect(login_page.username_input).to_be_visible()

    page.go_back(
        wait_until="domcontentloaded",
        timeout=60000
    )

    expect(login_page.username_input).to_be_visible(
        timeout=15000
    )

    expect(login_page.password_input).to_be_visible(
        timeout=15000
    )

    expect(page).to_have_url(
        LOGIN_URL,
        timeout=15000
    )

    expect(dashboard_page.dashboard_heading).not_to_be_visible()