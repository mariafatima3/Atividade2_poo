# 28) Você está criando um editor de texto simples. A classe Documento deve gerenciar o conteúdo de forma privada, 
# permitindo que o usuário adicione linhas de texto através de métodos públicos. 
# Tarefa: Crie uma classe Documento que: Tenha um atributo privado __conteudo, inicializado como uma lista vazia.
# Tenha um método público adicionar_linha(texto) que adiciona uma string à lista __conteudo.
# Tenha um método público ler_documento() que junta todas as linhas da lista com uma quebra de linha (\n) e retorna o texto completo.
# Crie um documento, adicione três linhas de texto e, em seguida, use ler_documento() para imprimir o conteúdo final.

class Documento:
    def __init__(self):
        self.__conteudo = []

    def adicionar_linha(self, texto):
         self.__conteudo.append(texto)

    def ler_documento(self):
        return "\n" .join(self.__conteudo)
    
documento = Documento()    
documento.adicionar_linha("Primeira linha do texto")
documento.adicionar_linha("Segunda linha do texto")
documento.adicionar_linha("Terceira linha do texto")
print(documento.ler_documento())


