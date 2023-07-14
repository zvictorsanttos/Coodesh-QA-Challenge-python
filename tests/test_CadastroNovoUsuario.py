import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

fake = Faker()
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

nome = fake.name()
email = fake.email()
driver.maximize_window()
driver.get("https://beta.coodesh.com/")
driver.implicitly_wait(5)

driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
driver.find_element(By.CLASS_NAME, "css-jm60sf").click()
elemento_nome = driver.find_element(By.ID, "field-6").send_keys(nome)
elemento_email = driver.find_element(By.ID, "field-7").send_keys(email)
driver.find_element(By.ID, "field-8").send_keys("Testeqa@123")
driver.find_element(By.CLASS_NAME, "css-jznrgy").click()
driver.find_element(By.CLASS_NAME, "css-18dmrac").click()
element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "d-block"))).click()
time.sleep(10)
element = driver.find_element(By.XPATH, "//*[@id='__next']/div[3]/div/div/div/div/div[1]/form/div[5]/div[2]/div[1]")
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.find_element(By.CSS_SELECTOR, "#__next > div.container.space-bottom-3.space-top-2.container > div > div > div > div > div.fade.p-0.tab-pane.active.show > form > div:nth-child(6) > div:nth-child(2) > div:nth-child(2) > div > input").send_keys("81952910699")
driver.find_element(By.ID, "address.city").send_keys("Vitoria de Santo Antão")
driver.find_element(By.ID, "home-office-integral").click()
driver.find_element(By.XPATH, "//*[@id='footer-portal']/div/div/button").click()
time.sleep(5)
dropdown_cor = Select(driver.find_element(By.ID,"race"))
dropdown_cor.select_by_value("noanswer")
dropdown_cor = Select(driver.find_element(By.ID,"gender"))
dropdown_cor.select_by_value("noanswer")
dropdown_cor = Select(driver.find_element(By.ID,"sexual_orientation"))
dropdown_cor.select_by_value("noanswer")
dropdown_cor = Select(driver.find_element(By.ID,"disabilities.type"))
dropdown_cor.select_by_value("none")
driver.find_element(By.XPATH, "//*[@id='__next']/div[3]/div/div/div/div/div[2]/form/div[1]/div[3]").click()
texto_visivel = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[text()="Saúde"]'))
)
texto_visivel.click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='footer-portal']/div/div/button[2]").click()

#Inicio do Score
driver.find_element(By.XPATH, "//*[@id='footer-portal']/div/div/a").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='footer-portal']/div/div/button[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='__next']/div[3]/div/div/form/table/tbody/tr[2]/td/div/div[3]").click()
driver.find_element(By.XPATH, "//*[@id='footer-portal']/div/div/button[2]").click()
driver.find_element(By.XPATH, "//*[@id='footer-portal']/div/div/a").click()

#Iniciando Pesquisa de Vaga
driver.find_element(By.XPATH, "//*[@id='content']/div/div/div[2]/div[2]/div[3]/a/div/div/h3").click()
driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/form/div/div[1]/div/input").send_keys("Mary Flower - Factory Software")
driver.find_element(By.XPATH, "//*[@id='content']/div/div[1]/form/div/div[2]/div/input").send_keys("Belo Horizonte")
driver.find_element(By.XPATH, "//*[@id='content']/div/div[1]/form/div/div[3]/button").click()
time.sleep(20)



