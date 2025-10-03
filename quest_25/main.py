# 25) Um sistema de Configuracao precisa armazenar diversas propriedades em um dicionário privado. 
# No entanto, a chave "id" é reservada e não pode ser alterada ou definida pelo usuário.Tarefa: Crie uma classe Configuracao que:
# Tenha um atributo privado __propriedades inicializado como um dicionário vazio.
# Tenha um método público definir_propriedade(chave, valor) que adiciona o par chave-valor ao dicionário, a menos que a chave seja "id". 
# Se for "id", o método deve imprimir "Erro: a chave 'id' é protegida."
# Instancie a classe, tente definir a propriedade "id" e, em seguida, defina uma propriedade válida como "tema" com o valor "escuro".

class Configuracao:
    def __init__(self):
        self.__propriedades = {}

    def definir_propriedade(self, chave, valor):
        if chave == "id":
            print( "Erro: a chave 'id' é protegida.")
        else:
            self.__propriedades[chave] = valor

    def propriedade_valida(self):
     return self.__propriedades 

configuracao = Configuracao()
configuracao.definir_propriedade("id", 1815)
configuracao.definir_propriedade("tema", "escuro")
print(configuracao.propriedade_valida())