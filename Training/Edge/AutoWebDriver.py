from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options, executable_path=EdgeChromiumDriverManager().install())

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://curtainmatrix.co.uk/finaltesting")