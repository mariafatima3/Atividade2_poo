# 21) Uma empresa de segurança precisa de uma classe Cofre para gerenciar senhas. O cofre deve proteger a senha de acessos externos diretos. 
# Tarefa: Crie uma classe Cofre que: Receba uma senha no construtor e a armazene em um atributo privado (ex: __senha).
# Tenha um método público verificar_senha(tentativa) que recebe uma string e retorna True se a tentativa for igual à senha armazenada, e False caso contrário.
# Após criar a classe, instancie um cofre com a senha "1234" e teste o método verificar_senha com uma tentativa correta e uma incorreta.

class Cofre:
    def __init__(self, senha):
        self.__senha = senha

    def verificar_senha(self, tentativa):
     return tentativa == self.__senha 
     
cofre = Cofre(1234)

print(cofre.verificar_senha(1234))
print(cofre.verificar_senha(4321))

