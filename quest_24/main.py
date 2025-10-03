# 24) Um sistema de inventário usa um Produto com um código interno que não deve ser acessado.
# Contudo, em Python, o "name mangling" (desfiguração de nome) permite um acesso "indireto".
# Tarefa: Crie uma classe Produto com um atributo privado __codigo_interno inicializado com "XYZ987". Instancie a classe.
# Tente acessar o atributo diretamente (produto.__codigo_interno) e observe o AttributeError.
# Acesse o atributo usando a sintaxe de "name mangling" (produto._Produto__codigo_interno) e imprima seu valor.
# Explique em um comentário por que isso funciona e por que essa prática deve ser evitada.


class Produto:
    def __init__(self):
        self.__codigo_interno = "XYZ987"
   
produto = Produto()
try:
   print(produto.__codigo_interno)
except AttributeError as e:
    print(f"Erro: ao acessar  diretamente: {e}")
print( "Acesso via name mangling", produto._Produto__codigo_interno )

# Funciona porque o uso de dois underlines (_ _) em atributos ativa o  "Name Mangling".
#  Isso não impede totalmente o acesso, impede apenas o acesso direto.
# Essa prática de ser evitada para não gerar confusão  e problemas na manutenção do código.

