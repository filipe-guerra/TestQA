import unittest
import time
from getpage import *
from getDatabase import *

class ValidateEmail(unittest.TestCase):
    def setUp(self):
        fillAllFields()
        #Remover o email de cadastro da DB

    def test_ArrobaMissing(self):
        cadSeuEmail.clear()
        cadSeuEmail.send_keys("abcdef")
        cadCadastrarButton.click()
        self.assertEqual("Formulário de Login e Registro com HTML5 e CSS3", driver.title)
    
    def test_ArrobaLastPosition(self):
        cadSeuEmail.clear()
        cadSeuEmail.send_keys("abcdef@")
        cadCadastrarButton.click()
        self.assertEqual("Formulário de Login e Registro com HTML5 e CSS3", driver.title)

    def test_ArrobaFirstPosition(self):
        cadSeuEmail.clear()
        cadSeuEmail.send_keys("@abcdef")
        cadCadastrarButton.click()
        self.assertEqual("Formulário de Login e Registro com HTML5 e CSS3", driver.title)
    
    def test_DoubleArroba(self):
        cadSeuEmail.clear()
        cadSeuEmail.send_keys("ab@cd@ef")
        cadCadastrarButton.click()
        self.assertEqual("Formulário de Login e Registro com HTML5 e CSS3", driver.title)
    
class ValidatePassword(unittest.TestCase):
    def setUp(self):
        fillAllFields()

    def test_PasswordOK(self):
        cadSenha.clear()
        cadSenha.send_keys("A!1cde")
        cadCadastrarButton.click()
        self.assertEqual("Formulário de Login e Registro com HTML5 e CSS3", driver.title)

    def test_Password5digts(self):
        cadSenha.clear()
        cadSenha.send_keys("A!1cd")
        cadCadastrarButton.click()
        self.assertEqual("Formulário de Login e Registro com HTML5 e CSS3", driver.title)

    def test_PasswordUpperCase(self):
        cadSenha.clear()
        cadSenha.send_keys("a!1cde")
        cadCadastrarButton.click()
        self.assertEqual("Formulário de Login e Registro com HTML5 e CSS3", driver.title)

    def test_PasswordSpecial(self):
        cadSenha.clear()
        cadSenha.send_keys("Ab1cde")
        cadCadastrarButton.click()
        self.assertEqual("Formulário de Login e Registro com HTML5 e CSS3", driver.title)
    
    def test_PasswordNumber(self):
        cadSenha.clear()
        cadSenha.send_keys("A!bcde")
        cadCadastrarButton.click()
        self.assertEqual("Formulário de Login e Registro com HTML5 e CSS3", driver.title)
    
class ValidateCEP(unittest.TestCase):
    def setUp(self):
        fillAllFields()
    
    def test_CEP1incompleted(self):
        cadCEP.clear()
        cadCEP.send_keys("1234")
        cadCadastrarButton.click()
        self.assertEqual("Formulário de Login e Registro com HTML5 e CSS3", driver.title)
    
    def test_CEP2incompleted(self):
        cadCEP2.clear()
        cadCEP2.send_keys("12")
        cadCadastrarButton.click()
        self.assertEqual("Formulário de Login e Registro com HTML5 e CSS3", driver.title)
    
if __name__ == '__main__':
    unittest.main()