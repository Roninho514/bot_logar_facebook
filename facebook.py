from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import usuario,senha
from time import sleep
facebook = 'https://www.facebook.com/'
navegador = webdriver.Chrome()
navegador.get(facebook)
navegador.implicitly_wait(5)
emailElement = navegador.find_element_by_id('email')
senhaElement = navegador.find_element_by_id('pass')
botaoEntrar = navegador.find_elements_by_id('u_0_d_yy')
emailElement.click()
emailElement.send_keys(usuario)
sleep(1)
senhaElement.click()
senhaElement.send_keys(senha)
senhaElement.send_keys(Keys.ENTER)
