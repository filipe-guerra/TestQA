import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def setElement_Text(element, text):
    elem = driver.find_element_by_id(element)
    elem.send_keys(text)

driver = webdriver.Chrome(r'C:\Users\Filipe\Documents\Python\SeleniumDriver\chromedriver.exe')

driver.get("https://letsbomfin.github.io/cadastro.github.io/")

print(driver.title)
    
setElement_Text("nome_cad", "banana")

cadastro = driver.find_elements_by_id('cadastro')
print(cadastro)

# Tela de cadastro
#Seu nome
cadSeuNome = driver.find_element_by_id("nome_cad")
print(cadSeuNome.get_attribute("value"))
print(cadSeuNome.get_attribute("required"))

#Seu email
cadSeuEmail = driver.find_element_by_id("email_cad")

#Estado
cadEstado = driver.find_element_by_id("estado_cad")
print(cadEstado.get_attribute("required"))

#Cidade
cadCidade = driver.find_element_by_id("cidade_cad")

#Sua rua
cadRua = driver.find_element_by_id("rua_cad")

#Bairro
cadBairro = driver.find_element_by_id("bairro_cad")

#CEP
cadCEP = driver.find_element_by_name("cep")
print(cadCEP.get_attribute("required"))

#Sua senha
cadSenha = driver.find_element_by_id("senha_cad")
cadSenha.send_keys("abcdef")
print(cadSenha.get_attribute("value"))
#Cadastrar button
cadCadastrarButton = driver.find_element_by_xpath("//input[@value='Cadastrar']")
#clear_button = driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")

#Resetar button
cadResetarButton = driver.find_element_by_xpath("//input[@value='Resetar']")


#Tela de login ###############################################
#Seu nome
loginSeuNome = driver.find_element_by_id("nome_login")

#Seu email
loginSeuEmail = driver.find_element_by_id("email_login")

#Logar button
loginLogarButton = driver.find_element_by_xpath("//input[@value='Logar']")

#Cadastre button
loginCadastreButton = driver.find_element_by_id("cadastre_botton")

#Ja tem conta - Link para o login
cadLoginLink = driver.find_element_by_xpath("//a[@href='#paralogin']")
print("ok")
cadLoginLink.click()
loginSeuNome.send_keys("logintest")
time.sleep(5)

# cadSeuEmail.send_keys("abcdef")
# cadCadastrarButton.click()
# time.sleep(4)

driver.quit
