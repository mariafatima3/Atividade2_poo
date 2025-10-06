# 27) Um Termostato inteligente controla a temperatura de um ambiente. 
# A temperatura é um estado interno (privado) que só deve ser lido através de um método que formata a informação para o usuário. 
# Tarefa: Crie uma classe Termostato que: Receba uma temperatura inicial no construtor e a armazene em um atributo privado __temperatura.
# Tenha um método público descrever() que retorna uma string formatada, como: "Temperatura atual: 25 graus Celsius."
# Instancie um termostato com 23 graus e imprima o resultado do método descrever().

class Termostato:
    def __init__(self, temperatura_inicial):
        self.__temperatura = temperatura_inicial

    def descrever(self):
        return f"Temperatura atual: {self.__temperatura} graus Celsius."


termostato = Termostato(23)
print(termostato.descrever())

