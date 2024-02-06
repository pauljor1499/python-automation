from assertpy import assert_that
import pdb
import pytest

class Login:
    @pytest.fixture
    def admin_login(page):
        page.goto("/")
        page.click("//span[contains(.,'Log In')]")
        assert_that(page.is_visible("//div[@class='title'][contains(.,'Log In')]")).is_true()
        assert_that(page.is_visible("//input[contains(@type,'email')]")).is_true()
        assert_that(page.is_visible("//input[contains(@type,'password')]")).is_true()
        print('Hello')