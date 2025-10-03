# 26) Em um jogo, a pontuacao de um Jogador só pode aumentar. Ela deve ser privada para impedir que valores negativos sejam somados ou que a pontuação seja zerada indevidamente. 
# Tarefa: Crie uma classe Jogador que: Receba um nome (público) e inicialize um atributo privado __pontuacao com 0.
# Tenha um método público adicionar_pontos(pontos) que aumenta a pontuação apenas se o valor de pontos for positivo. Se for negativo ou zero, o método não faz nada.
# Tenha um método público ver_pontuacao() que retorna a pontuação atual. Crie um jogador, adicione 50 pontos, tente adicionar -10 pontos e exiba a pontuação final.

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.__pontuacao = 0
    def adicionar_pontos(self, pontos):
        if pontos > 0:
            self.__pontuacao += pontos
    
    def ver_pontuacao(self):
       return self.__pontuacao
    
jogador = Jogador("Miquel")
jogador.adicionar_pontos(50)
jogador.adicionar_pontos(-10)

print(f"Pontuação Final: {jogador.nome} : {jogador.ver_pontuacao()} pontos.")

    
        