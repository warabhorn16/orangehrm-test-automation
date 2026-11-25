
import pytest
from pathlib import Path

from pages.login_page import LoginPage
from config.settings import BASE_URL


SCREENSHOT_DIR = Path("screenshots")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            SCREENSHOT_DIR.mkdir(exist_ok=True)

            screenshot_name = (
                item.nodeid.replace("/", "_").replace("::", "_")
            )

            screenshot_path = SCREENSHOT_DIR / f"{screenshot_name}.png"

            try:
                page.screenshot(
                    path=str(screenshot_path),
                    full_page=True
                )
            except Exception as error:
                print(f"Could not capture failure screenshot: {error}")


@pytest.fixture
def login_page(page):
    page.goto(
        BASE_URL + "/web/index.php/auth/login",
        wait_until="domcontentloaded"
    )
    return LoginPage(page)
