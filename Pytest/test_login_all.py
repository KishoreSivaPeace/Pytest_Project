from allure_commons.types import AttachmentType

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def log_on_failure(request, chrome_driver):
    yield
    item = request.node
    driver = chrome_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)


def get_data():
    return [
        ("KISHORESIVADB", "KishoreSiva", "1103"),
        ("KISHORESIVADB", "PeaceArt", "1103")
    ]


@pytest.fixture()
def chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())

    driver.maximize_window()
    yield driver
    # driver.minimize_window()
    # driver.quit()


@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.parametrize("DBname, username, password", get_data())
def test_login(chrome_driver, DBname, username, password):
    driver = chrome_driver
    driver.get("https://curtainmatrix.co.uk/finaltesting")
    driver.find_element(By.XPATH, "//*[@id='companyname']").send_keys(DBname)
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
    driver.find_element(By.XPATH,
                        "/html/body/app-root/main/section/lib-login/div/div/div/div/div[2]/div/form/div[4]/button[1]").click()
    # assert 1 == 2
