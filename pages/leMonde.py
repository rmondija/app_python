from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

url = "https://www.lemonde.fr/"
driver = webdriver.Chrome() # chemin du webdriver chrome
driver.get(url)
sleep(2)
driver.find_element(By.CLASS_NAME,"gdpr-lmd-button.gdpr-lmd-button--big.gdpr-lmd-button--slate-darker").click()
sleep(2)
#click sur le bouton search
driver.find_element(By.CLASS_NAME,"Nav__search.icon__search").click()
sleep(2)
# cherche Python dans la barre de recherche
driver.find_element(By.ID,"search_keywords").send_keys('Python'+Keys.ENTER)

articles2 = driver.find_element(By.CLASS_NAME,"js-river-search")

# url de l'image
articles2.find_elements(By.TAG_NAME, "section")[0].find_element(By.TAG_NAME,"figure").find_element(By.TAG_NAME,"source").get_attribute("srcset")

driver.quit