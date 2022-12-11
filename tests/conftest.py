import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_managmet():
    browser.config.timeout = 3.0
    browser.config.base_url = 'https://www.google.com'
    yield

    browser.quit()