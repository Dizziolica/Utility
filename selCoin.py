from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

optioon = Options()
optioon.add_argument("--headless")
driver = webdriver.Chrome(options=optioon)

moedas = ["Vao Dólar", "Valo Peso Argentino", "valor won"]

for moeda in moedas:
    driver.get(f"https://google.com/search?q={moeda}&hoje")
    valor = driver.find_element(By.CLASS_NAME, "DFlfde.SwHCTb")
    print(f"moeda {moeda} equivae {valor.text}")

driver.quit()
