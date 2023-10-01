import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def setting_size_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 4.0
    browser.config.window_width = 1600
    browser.config.window_height = 900



