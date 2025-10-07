# 30) Um sistema de Log precisa registrar mensagens com um timestamp. O acesso direto à lista de mensagens é proibido para garantir que toda mensagem passe pelo processo 
# de adição de timestamp. Tarefa: Crie uma classe Log que: Importe o módulo datetime. Tenha um atributo privado __mensagens, inicializado como uma lista vazia.
# Tenha um método público registrar(mensagem) que cria uma string formatada como "{timestamp} - {mensagem}" e a adiciona à lista privada. Use datetime.datetime.now().
# Tenha um método público exibir_logs() que imprime cada mensagem da lista em uma nova linha. Instancie a classe, registre duas mensagens e, ao final, exiba os logs.

import datetime
class Log:
    def __init__(self):
        self.__mensagens = []

    def registrar(self, mensagem):
        timestamp = datetime.datetime.now()
        log_formatado = f"{timestamp} - {mensagem}"
        self.__mensagens.append(log_formatado)

    def exibir_logs(self):
        for mensagem in self.__mensagens:
          print(mensagem)
log = Log()
log.registrar("Primeira mensagem")
log.registrar("Segunda mensagem")
log.exibir_logs()
