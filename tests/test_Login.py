import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://beta.coodesh.com/")
driver.implicitly_wait(5)

driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
driver.find_element(By.ID, "field-6").send_keys("testeqachallenger@hotmail.com")
driver.find_element(By.ID, "field-7").send_keys("TesteQA@1234")
driver.find_element(By.CLASS_NAME,"css-18dmrac").click()
texto_visivel = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[text()="Meu Perfil"]'))
)
texto_visivel.is_displayed()

time.sleep(10)







