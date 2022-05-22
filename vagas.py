from selenium import webdriver
import time

DRIVER_PATH = 'C:/Users/Vaivoa/Downloads/chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://www.sp.senac.br/recruPortal/portal/mural")

time.sleep(5)
if 'Senac Campinas' in driver.page_source:
    {
    print('Achei')
    }
driver.quit()
