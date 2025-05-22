import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
import undetected_chromedriver as uc
import undetected_geckodriver as uf

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default = "chrome", help = "Specify the browser: chrome or firefox or edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = uc.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported Browser")
    return driver


def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'Ecommerce Project, nopcommerce'
    config.stash[metadata_key] ['Test Module Name'] = 'Admin Login Tests'
    config.stash[metadata_key] ['Tester Name'] = 'Prashun'
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

