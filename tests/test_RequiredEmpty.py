import unittest
from getpage import *

class TelaCadastro(unittest.TestCase):

    def test_PageOppened(self):
        self.assertEqual("Formulário de Login e Registro com HTML5 e CSS3", driver.title)
    
    def test_CadastroEmpty(self):
        clearAllFields()
        cadCadastrarButton.click()
        self.assertEqual("Formulário de Login e Registro com HTML5 e CSS3", driver.title)
    # @classmethod
    # def tearDownClass(self):
    #     driver.close()
    #     driver.quit()

class ResetButtonTest(unittest.TestCase):
    # @classmethod
    # def setUpClass(self):
    fillAllFields()
    cadResetarButton.click()

    def test_seuNomeEmpty(self):
        assert cadSeuNome.get_attribute("value") == ""

    def test_seuEmailEmpty(self):
        assert cadSeuEmail.get_attribute("value") == ""

    def test_estadoEmpty(self):
        assert cadEstado.get_attribute("value") == ""

    def test_cidadeEmpty(self):
        assert cadCidade.get_attribute("value") == ""
    
    def test_ruaEmpty(self):
        assert cadRua.get_attribute("value") == ""
    
    def test_bairroEmpty(self):
        assert cadBairro.get_attribute("value") == ""

    def test_cepEmpty(self):
        assert cadCEP.get_attribute("value") == ""
    
    def test_cep2Empty(self):
        assert cadCEP2.get_attribute("value") == ""
    
    def test_senhaEmpty(self):
        assert cadSenha.get_attribute("value") == ""
    # @classmethod
    # def tearDownClass(self):
    #     driver.stop_client()
    #     driver.close()
    #     driver.quit()


    # Teste manual se o botao esta mandando para o lugar certo
    # def test_loginButtonClick(self):
    #     cadLoginLink.click()

class AllItensRequired(unittest.TestCase):

    def test_seuNomeRequired(self):
        self.assertTrue(cadSeuNome.get_attribute("required"))

    def test_seuEmailRequired(self):
        self.assertTrue(cadSeuEmail.get_attribute("required"))

    def test_estadoRequired(self):
        self.assertTrue(cadEstado.get_attribute("required"))

    def test_cidadeRequired(self):
        self.assertTrue(cadCidade.get_attribute("required"))
    
    def test_ruaRequired(self):
        self.assertTrue(cadRua.get_attribute("required"))
    
    def test_bairroRequired(self):
        self.assertTrue(cadBairro.get_attribute("required"))

    def test_cepRequired(self):
        self.assertTrue(cadCEP.get_attribute("required"))
    
    def test_cep2Required(self):
        self.assertTrue(cadCEP2.get_attribute("required"))
    
    def test_senhaRequired(self):
        self.assertTrue(cadSenha.get_attribute("required"))
        
if __name__ == '__main__':
    unittest.main()


