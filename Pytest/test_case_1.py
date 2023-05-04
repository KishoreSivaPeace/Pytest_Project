import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from configreader import readconfig


def test_login(chrome_driver):
    driver = chrome_driver
    driver.get(readconfig("URL", "final_testing"))
    driver.find_element(By.XPATH, "//*[@id='companyname']").send_keys(readconfig("user_info", "company_name"))
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys(readconfig("user_info", "username1"))
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(readconfig("user_info", "password"))
    driver.find_element(By.XPATH,
                        "/html/body/app-root/main/section/lib-login/div/div/div/div/div[2]/div/form/div[4]/button[1]").click()
    # allure.attach(driver.get_screenshot_as_png(),name="Error", attachment_type=AttachmentType.PNG)
