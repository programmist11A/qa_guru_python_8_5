import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_manager():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 960
    browser.config.window_height = 540