#criar lista com produtos

"""produtos=["mouse", "teclado", "monitor"]

print (produtos[0])

#append adiciona o elemento ao final da lista
produtos.append("headset")

#insert adiciona o elemento em uma posição especifica
produtos.insert(1, "webcam")

#remove(),  remove um elemento especifico
produtos.remove("mouse")

#pop() remove pelo seu indice
produtos.pop(1)

#altera o valor de um elemento ultilizando seu indice
produtos[0] = "teclado gamer" 

#len() retorna a quantidade de elemento
print("Quantidade de produtos:", len(produtos)) #4

#in() verifica se determinado elemento existe
if "monitor" in produtos:
    print("monitor encontrado!")

#for() percorre todos os elementos da lista
for produto in produtos :
    print ("\n=== LISTA DE PRODUTOS ===")


    1. Listas — Lista de compras
Crie um programa que permita organizar uma lista de compras.
O programa deve:    Criar uma lista vazia chamada compras.  Adicionar 3 produtos utilizando append().
Adicionar mais um produto na segunda posição utilizando insert().  Exibir todos os produtos utilizando for.  Remover um produto utilizando remove().  Exibir todos os produtos utilizando for.
Mostrar quantos produtos existem na lista utilizando"""

lista=[]

lista.append("sabonete")
lista.append("condicionador")
lista.append("PlayStation")

lista.insert(1, "chuveiro" )

for produto in lista :
    print (produto)

lista.remove("sabonete")

for produto in lista :
    print (produto)
