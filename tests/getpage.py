from selenium import webdriver
from selenium.webdriver.common.keys import Keys


silentMode = True

#Silent mode
if silentMode:
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument("--headless") # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox') # Bypass OS security model
    options.add_argument('--disable-gpu')  # applicable to windows os only
    options.add_argument('start-maximized') # 
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\Filipe\Documents\Python\SeleniumDriver\chromedriver.exe')
else:
    driver = webdriver.Chrome(r'C:\Users\Filipe\Documents\Python\SeleniumDriver\chromedriver.exe')

del silentMode

driver.get("https://letsbomfin.github.io/cadastro.github.io/")


# Tela de cadastro
#Seu nome
cadSeuNome = driver.find_element_by_id("nome_cad")

#Seu email
cadSeuEmail = driver.find_element_by_id("email_cad")

#Estado
cadEstado = driver.find_element_by_id("estado_cad")

#Cidade
cadCidade = driver.find_element_by_id("cidade_cad")

#Sua rua
cadRua = driver.find_element_by_id("rua_cad")

#Bairro
cadBairro = driver.find_element_by_id("bairro_cad")

#CEP
cadCEP = driver.find_element_by_name("cep")

#CEP2
cadCEP2 = driver.find_element_by_name("cep2")

#Sua senha
cadSenha = driver.find_element_by_id("senha_cad")

#Cadastrar button
cadCadastrarButton = driver.find_element_by_xpath("//input[@value='Cadastrar']")
#clear_button = driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")

#Resetar button
cadResetarButton = driver.find_element_by_xpath("//input[@value='Resetar']")

#Ja tem conta - Link para o login
cadLoginLink = driver.find_element_by_xpath("//a[@href='#paralogin']")

#Tela de login ###############################################
#Seu nome
loginSeuNome = driver.find_element_by_id("nome_login")

#Seu email
loginSeuEmail = driver.find_element_by_id("email_login")

#Logar button
loginLogarButton = driver.find_element_by_xpath("//input[@value='Logar']")

#Cadastre button
loginCadastreButton = driver.find_element_by_id("cadastre_botton")

def fillAllFields():
    clearAllFields()
    cadSeuNome.send_keys("Nome")
    cadSeuEmail.send_keys("teste@test.com")
    cadEstado.send_keys("MG")
    cadCidade.send_keys("Belo Horizonte")
    cadRua.send_keys("Pernambuco")
    cadBairro.send_keys("Savassi")
    cadCEP.send_keys("30882")
    cadCEP2.send_keys("550")
    cadSenha.send_keys("123456")

def clearAllFields():
    cadSeuNome.clear()
    cadSeuEmail.clear()
    cadEstado.clear()
    cadCidade.clear()
    cadRua.clear()
    cadBairro.clear()
    cadCEP.clear()
    cadCEP2.clear()
    cadSenha.clear()
