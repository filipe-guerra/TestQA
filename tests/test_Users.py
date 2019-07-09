import unittest
import random
from getpage import *
from getDatabase import *


class UsersTests(unittest.TestCase):
    def test_EmailExistDatabase(self):
        fillAllFields()
        cadSeuEmail.clear()
        randomNumber = random.randint(0, len(listUsers))
        cadSeuEmail.send_keys(listUsers[randomNumber].email)
        cadCadastrarButton.click()
        self.assertEqual("Email já cadastrado", driver.title)
