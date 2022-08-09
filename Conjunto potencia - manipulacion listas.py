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


def factorial(n):
    if (n==0):
        return 1
    else:
        return factorial(n-1)*n
    
def total_combinaciones(n,r):
        return (factorial(n))/(factorial(r)*factorial(n-r))

print(f"Total saludos en un grupo de 4 personas {total_combinaciones(4,2)}")    

class persona:
    def __init__(self, nombre,sexo):
        self.nombre = nombre
        self.sexo = sexo
    def __str__(self):
        return self.nombre

personitas = [
    persona('Angela','F'),
    persona('Esperanza','F'),
    persona('Lorelei','F'),
    persona('Anya','F'),
    persona('Melquiadez','M'),
    persona('Renato','M'),
    persona('Pancho','M'),
    persona('Chucho','M'),
    persona('Pipe','M'),
    persona('Gonzo','M'),
    persona('Rufio','M'),
    
    ]        

        
def mostrar_personitas(per):
    
    for o in per:
        lista_personas=[]
        for p in o:
            lista_personas.append(p.nombre)
        print(lista_personas)
        
mostrar_personitas(conjunto_potencia(personitas))

def mostrar_combinaciones(lista,r):
    #filtrar el conjunto potencia por el valor r (opcion 1)
    #return list(filter(lambda x: (len(x)==r), conjunto_potencia(lista))) 
    #filtrar el conjunto potencia por el valor r (opcion 2)
    return [p for p in conjunto_potencia(lista) if(len(p)==r)]
print("Listado de saludos entre personas")
a = mostrar_personitas(mostrar_combinaciones(personitas,2))

#Formar equipos de 5 con un grupo de personas donde existen 7 hombres y 4 mujeres
#procedo normalmente: mostrar_combinaciones(...)

#Formar equipos con 2 hombres y 3 mujeres, con un grupo de personas donde existen 7 hombres y 4 mujeres
#



h = total_combinaciones(7,2)
m = total_combinaciones(4,3)
print(f"Total grupos de hombres {total_combinaciones(7,2)}")    
print(f"Total grupos de mujeres {total_combinaciones(4,3)}")    
print(f"Formar equipos con 2 hombres y 3 mujeres: {h*m}")
#????? Como genero el resultado de posibles equipos??????
#el tamaño del resultado deberia ser 84

