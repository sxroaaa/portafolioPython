#definir una lista 
lista=[]#esta lista esta vacia
lista2=[1, 2, 3, 4] 
print (lista2)
#acceder a una posicion especifica a travez del index
print(lista2[2])
#ultimo elemento de la lista
print(lista[-1])
#penultimo elemento de una lista
print(lista2[-2])
#modifica un elemento de una posicion
lista2[3]=15
print(lista2)
#recorrer la lista2 y multiplicar por 2 sus elementos
for i in lista2:
    print(1*2)
for index, i in enumerate(lista2):
    print(f"en la posicion {index} se encuentra el valor {i}")
    
numeros=[5, 9, 10]
generos=["jazz, Rock, djent"]