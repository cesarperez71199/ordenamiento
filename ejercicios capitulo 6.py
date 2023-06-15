# -*- coding: utf-8 -*-
"""
Created on Wed May 31 16:03:45 2023

@author: Cesar Perez
"""

# **********  CAPITULO 6  ***********


#ejercicio 6 


import math
import random



#Variables de vectores
x=[3,4,5]
y=[-2,-1,6]


#Variable temporal donde se guardara la suma de los vectores
suma=0


#for que hara la suma de los vectores
for i in range(len(x)):
    
    suma= suma + x[i]*y[i]      # suma= 0 + 3 * -2
                                # suma= -6 + 4* -1
                                # suma= -10 + 5*6
                                # suma= 20



print("El resultado del escalar de X y Y por el coseno es: ", math.cos(suma)
      



#Ejercicio 8

"""
a=[5,2]
b=[2,3]

factor=0

for i in range(len(a)):
    
    factor= factor + a[i]*b[i]
    
        
print("El trabajo de los vectores a y b es: ", factor, "Joules")

angulo= math.cos(factor)

print("El angulo es: ", angulo) 

"""



#Ejercicio 9


"""

#Genenera 20 numeros aleatorios y los almacena en una lista
numeros= [random.randint(0, 5) for _ in range(5)]


#Guardamos esa lista en una nueva variable 
vector= numeros 


#Guardamos la longitud de vector en la variable longitud 
longitud=len(vector)

print(vector)


#Inicializamos el for que ordenara los numeros 
for i in range(longitud-1):                     #Para i en el rango de la longitud-1 espacio
    
    menor=i                                     #En la variable menor guardaremos las posiciones 
                                                # que recorrera i
    
    for j in range(i+1, longitud):              #Para j en el rango de longitud 
    
        if vector [j]< vector[menor]:           #Si el numero en vector j es menor al numero en menor
                                                    
            menor=j                             #saltara a esta instruccion
            
       # En caso de no cumplirse se regresara al for j a comparar 
                                       # el numero de la siguiente posicion en j
            
    
    #Hazta que la sentencia anteior sea cierta entrara a a estas indicaciones 
    temp= vector[menor]             
    vector[menor]= vector[i]
    vector[i]=temp
    

print(vector)
            

"""


#Ejercicio 11



# Generar un vector aleatorio de 10 números
vector = [random.randint(1, 100) for _ in range(10)]
print("Vector aleatorio:", vector)



# Seleccionar el penúltimo elemento
penultimo = vector[-2]
print("Penúltimo elemento:", penultimo)

# Utilizar el algoritmo de búsqueda binaria
def busqueda_binaria(vector, elemento):
    izquierda = 0
    derecha = len(vector) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if vector[medio] == elemento:
            return medio
        elif vector[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

# Buscar el penúltimo elemento utilizando búsqueda binaria
indice = busqueda_binaria(vector, penultimo)
if indice != -1:
    print("El penúltimo elemento se encuentra en el índice:", indice)
else:
    print("El penúltimo elemento no se encuentra en el vector.")

    
    
    
    



            
            


