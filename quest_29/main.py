# 29) Para simular um Carro, o estado "ligado" ou "desligado" deve ser controlado por métodos, não por acesso direto, para evitar estados inconsistentes 
# (ex: acelerar com o carro desligado). Tarefa: Crie uma classe Carro que: Tenha um atributo privado __ligado, inicializado como False.
# Tenha um método público ligar() que muda __ligado para True. Tenha um método público desligar() que muda __ligado para False.
# Tenha um método público status() que retorna a string "Carro está ligado" se __ligado for True, e "Carro está desligado" caso contrário.
# Instancie um carro, chame o método ligar() e depois imprima seu status. Em seguida, chame desligar() e imprima o status novamente.

class Carro:
    def __init__(self):
        self.__ligado = False
        
    def ligar(self):
         self.__ligado = True
         
    def desligar(self):
          self.__ligado = False
    def status(self):
       if self.__ligado:
           return "Carro está ligado"
       else:
           return "Carro está desligado"
       
carro = Carro()
carro.ligar()
print(carro.status())
carro.desligar()
print(carro.status())

