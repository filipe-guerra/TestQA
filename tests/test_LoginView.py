# import unittest
# from getpage import *
# from getDatabase import *


# class UsersTests(unittest.TestCase):
#     def setUp(self):
#         cadLoginLink.click()
#         #Cadastrar usuario para testar

#     def test_LogarUserOk(self):
#         loginSeuNome.send_keys("teste@teste.com")
#         loginSeuEmail.send_keys("1Ab$cde")
#         loginLogarButton.click()
#         self.assertEqual("Bem vindo", driver.title)

#     def test_LogarUserNotOK(self):
#         loginSeuNome.send_keys("usuarioInvalido@teste.com")
#         loginSeuEmail.send_keys("1Ab$cde")
#         loginLogarButton.click()
#         self.assertNotEqual("Bem vindo", driver.title)

#     def test_LogarClickEmptyFields(self):
#         clearAllFields()
#         loginLogarButton.click()
#         self.assertEqual("Formulário de Login e Registro com HTML5 e CSS3", driver.title)
   
