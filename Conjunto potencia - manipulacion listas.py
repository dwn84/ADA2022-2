#Recorderis de manejo de listas en Python
datos = [1,2,3,4,5,6,7]#Lista circular doble
print(datos[0])
print(datos[5])
print(datos[:])
print(datos[-1])
print(datos[-2])
print(datos[:-1])
print(datos[-1:])
datos + [9] #concatenación de listas

def validarX(n):
    if(n%2==0):
        return True
    else:
        return False
#filtrado de lista (implica el mapeado)
resultado = filter(validarX,datos)  
print(list(resultado))
print(datos)

#Listas de compresion (mapeado y filtrado)

for x in datos:
    print(x)
for x in range(10):
    print(x)

c = [2 ** x for x in datos if(x%2==0)]#filtrado
print(c)

#[2, 4, 8, 16, 32, 64, 128]
#[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]


lista = [numero for numero in
	[numero**2 for numero in range(0,11)]
		if numero % 2 == 0]

print(lista)



mis_daticos= ['Lechuga','tomate','cebolla']


def conjunto_potencia(c):
    if(len(c)==0):
        return [[]]
    else:
        ultimo = conjunto_potencia(c[:-1])
        return ultimo + [listaC + [c[-1]] for listaC in ultimo]

print(conjunto_potencia(mis_daticos))    
#[[], ['Lechuga'], ['tomate'], ['Lechuga', 'tomate'], ['cebolla'], ['Lechuga', 'cebolla'], ['tomate', 'cebolla'], ['Lechuga', 'tomate', 'cebolla']]
