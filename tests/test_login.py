
import pytest

from playwright.sync_api import expect

from config.settings import LOGIN_URL, DASHBOARD_URL
from pages.dashboard_page import DashboardPage
from test_data.login_data import (
    VALID_USERNAME,
    VALID_PASSWORD,
    INVALID_USERNAME,
    INVALID_PASSWORD,
)


@pytest.mark.login
def test_TC001_password_masking(login_page):
    login_page.enter_password(VALID_PASSWORD)

    expect(login_page.password_input).to_have_attribute(
        "type", "password"
    )


@pytest.mark.login
def test_TC002_login_with_valid_credentials(login_page):
    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

    dashboard_page = DashboardPage(login_page.page)

    expect(login_page.page).to_have_url(DASHBOARD_URL)
    expect(dashboard_page.dashboard_heading).to_be_visible()


@pytest.mark.login
def test_TC003_login_with_enter_key(login_page):
    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.press_enter()

    dashboard_page = DashboardPage(login_page.page)

    expect(login_page.page).to_have_url(DASHBOARD_URL)
    expect(dashboard_page.dashboard_heading).to_be_visible()


@pytest.mark.login
def test_TC004_login_with_invalid_username(login_page):
    login_page.enter_username(INVALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

    expect(login_page.login_error).to_have_text(
        "Invalid credentials"
    )

    expect(login_page.page).to_have_url(LOGIN_URL)


@pytest.mark.login
def test_TC005_login_with_invalid_password(login_page):
    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(INVALID_PASSWORD)
    login_page.click_login()

    expect(login_page.login_error).to_have_text(
        "Invalid credentials"
    )

    expect(login_page.page).to_have_url(LOGIN_URL)


@pytest.mark.login
def test_TC006_login_with_empty_username(login_page):
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

    expect(login_page.username_validation_error).to_have_text(
        "Required"
    )

    expect(login_page.password_validation_error).to_have_count(0)

    expect(login_page.page).to_have_url(LOGIN_URL)


@pytest.mark.login
def test_TC007_login_with_empty_password(login_page):
    login_page.enter_username(VALID_USERNAME)
    login_page.click_login()

    expect(login_page.password_validation_error).to_have_text(
        "Required"
    )

    expect(login_page.username_validation_error).to_have_count(0)

    expect(login_page.page).to_have_url(LOGIN_URL)


@pytest.mark.login
def test_TC008_login_with_empty_username_and_password(login_page):
    login_page.click_login()

    expect(login_page.username_validation_error).to_have_text(
        "Required"
    )

    expect(login_page.password_validation_error).to_have_text(
        "Required"
    )

    expect(login_page.page).to_have_url(LOGIN_URL)