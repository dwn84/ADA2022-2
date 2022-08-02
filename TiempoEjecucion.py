import time
import matplotlib.pyplot as grafica


tiempos_ejecucion =[]

for i in range(1,1200000000000):
    
    tiempo_inicial = time.time()
    
    for j in range(1,i):
        n = i

    tiempo_final = time.time()
    duracion_total = tiempo_final -tiempo_inicial
    tiempos_ejecucion.append(duracion_total)
    
grafica.plot(tiempos_ejecucion)

#print(f"Duracion total del proceso {duracion_total}")
