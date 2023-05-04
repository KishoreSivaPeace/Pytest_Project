import params as params
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="session")
def chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    yield driver


@pytest.fixture(scope="session")
def edge_driver():
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Edge(options=options, executable_path=EdgeChromiumDriverManager().install())
    driver.maximize_window()
    yield driver


@pytest.fixture(scope="session")
def firefox_driver():
    options = webdriver.FirefoxOptions()
    options.add_experimental_option("detach", True)
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    yield driver


@pytest.fixture(params=["chrome", "edge"], scope="session")
def get_browsers(request):
    global driver
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
    if request.param == "edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Edge(options=options, executable_path=EdgeChromiumDriverManager().install())

    driver.maximize_window()
    yield driver
