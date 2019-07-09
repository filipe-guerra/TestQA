listUsers = []

class Cadastros():
    def __init__(self, nome, email, estado, cidade, rua, bairro, cep1, cep2, senha):
        self.nome = nome
        self.email = email
        self.estado = estado
        self.rua = rua
        self.bairro = bairro
        self.cep1 = cep1
        self.cep2 = cep2
        self.password = senha
        
user1 = Cadastros("Joao", "joao@test.com", "SP", "Suzano", "Rua A", "Centro", "20052", "005", "9di#kC")
user2 = Cadastros("Maria", "maria@test.com", "RJ", "Petropolis", "Avenida Alpha", "Lourdes", "10088", "200", "jpdE4*")

listUsers.append(user1)
listUsers.append(user2)
