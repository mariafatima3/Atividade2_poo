# 23) Para um sistema de cadastro, a classe Usuario precisa validar o formato do e-mail antes de alterá-lo. O atributo de e-mail deve ser privado para forçar o uso da validação. 
# Tarefa: Crie uma classe Usuario que: Receba nome (público) e email (privado) no construtor.
# Tenha um método público alterar_email(novo_email) que só modifica o atributo de e-mail se o novo_email contiver o caractere "@".
#  Caso contrário, deve imprimir uma mensagem de erro. Crie uma instância de Usuario. 
# Tente alterar o e-mail para um valor inválido (ex: "email-invalido") e depois para um válido (ex: "novo@email.com").

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.__email = email

    def alterar_email(self, novo_email):
        if "@" in novo_email:
            self.__email = novo_email
            print(f"E-mail alterado com sucesso para: {self.__email}")
        else:
            print("Erro: E-mail inválido. Deve conter o caractere '@'.")

    def acessar_email(self):
        return self.__email
    
usuario = Usuario("maria", "maria@email.com")
usuario.alterar_email("maria_email.com")
print(f"Email atual após tentativa inválida: {usuario.acessar_email()}")
usuario.alterar_email("maria@email.com")
print(f"Email atual após alteração válida: {usuario.acessar_email()}")

