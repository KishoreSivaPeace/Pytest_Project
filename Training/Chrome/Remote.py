import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

driver.maximize_window()

driver.get("https://curtainmatrix.co.uk/finaltesting")
driver.find_element(By.XPATH, "//*[@id='companyname']").send_keys("KISHORESIVADB")
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("1103")
driver.find_element(By.XPATH, "/html/body/app-root/main/section/lib-login/div/div/div/div/div[2]/div/form/div[4]/button[1]").click()
# driver.find_element(By.XPATH, "/html/body/app-root/main/section/app-dashboard-new/app-navbar/div/mat-toolbar-row/div/div[2]/a[3]/a/p").click()
# driver.find_element(By.XPATH, "//*[@id='mat-menu-panel-1']/div/button[2]").click()
# driver.find_element(By.XPATH, "//*[@id='settingscroll']/div[2]/div/div/div/div[2]/div[1]/div/a").click()
# driver.find_element(By.XPATH, "/html/body/app-root/main/section/app-product/div[1]/div/button").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//*[@id='productname']").send_keys("Automation 2")
# driver.find_element(By.XPATH, "//*[@id='pcode']").send_keys("A2")
# element = driver.find_element(By.XPATH, "//*[@id='pcode']")
# element.send_keys(Keys.TAB, Keys.TAB, Keys.ENTER, Keys.ARROW_DOWN, Keys.ENTER)
# driver.find_element(By.XPATH, "//*[@id='savegeneralinfoButton']").click()
