from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(15)

driver.get("https://curtainmatrix.co.uk/finaltesting")
driver.get("https://curtainmatrix.co.uk/finaltesting")
driver.find_element(By.XPATH,"//*[@id='companyname']").send_keys("KISHORESIVADB")
driver.find_element(By.CSS_SELECTOR,"#username").send_keys("admin")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("1103")
driver.find_element(By.XPATH,"/html/body/app-root/main/section/lib-login/div/div/div/div/div[2]/div/form/div[4]/button[1]").click()