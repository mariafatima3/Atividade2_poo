# 22) Em uma rede social, uma postagem (PostRedeSocial) pode receber curtidas. 
# O número de curtidas deve ser encapsulado para que só possa ser incrementado, e não definido para um número qualquer diretamente.
# Tarefa: Crie uma classe PostRedeSocial que: Receba o texto da postagem (público) no construtor. Inicialize um atributo privado __curtidas com o valor 0.
# Tenha um método público curtir() que incrementa o contador __curtidas em 1. Tenha um método público ver_curtidas() que retorna o número atual de curtidas.
# Crie uma postagem, chame o método curtir() três vezes e, ao final, imprima o número total de curtidas usando ver_curtidas().

class PostRedeSocial:
    def __init__(self, texto):
        self.texto = texto
        self.__curtidas = 0
    
    def  curtir(self):
        self. __curtidas += 1

    def ver_curtidas(self):
        return  self.__curtidas
    
postagem = PostRedeSocial("Curtidas:")
postagem.curtir()
postagem.curtir()
postagem.curtir()

print("Total de curtidas:", postagem.ver_curtidas())


