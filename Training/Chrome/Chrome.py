from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
ser_obj = Service("G:/Sivakumar/Pytest Automation/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://curtainmatrix.co.uk/finaltesting")
driver.find_element(By.XPATH,"//*[@id='companyname']").send_keys("KISHORESIVADB")
driver.find_element(By.CSS_SELECTOR,"#username").send_keys("admin")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("1103")
driver.find_element(By.XPATH,"/html/body/app-root/main/section/lib-login/div/div/div/div/div[2]/div/form/div[4]/button[1]").click()
