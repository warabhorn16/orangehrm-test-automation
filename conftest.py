
import pytest

from pages.login_page import LoginPage
from config.settings import BASE_URL


@pytest.fixture
def login_page(page):
    page.goto(BASE_URL + "/web/index.php/auth/login")

    return LoginPage(page)
