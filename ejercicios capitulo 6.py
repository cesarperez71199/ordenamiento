# -*- coding: utf-8 -*-
"""
Created on Wed May 31 16:03:45 2023

@author: Cesar Perez
"""

#Ordenamiento de vectores

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
            

    
    



            
            


