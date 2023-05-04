from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(15)

driver.get("https://curtainmatrix.co.uk/finaltesting")
CompanyName = driver.find_element(By.XPATH,"//*[@id='companyname']")
CompanyName.send_keys("KISHORESIVADB")
UserName = driver.find_element(By.CSS_SELECTOR,"#username")
UserName.send_keys("admin")
Password = driver.find_element(By.CSS_SELECTOR,"#password")
Password.send_keys("1103")
Login = driver.find_element(By.XPATH,"/html/body/app-root/main/section/lib-login/div/div/div/div/div[2]/div/form/div[4]/button[1]")
Login.click()
