#SETS

# Contiene: 'cat', 'dog', 'goldfish', 'canary' y otro 'cat' duplicado
animales = {'gato', 'perro', 'pez dorado', 'canario', 'gato'}

#el duplicado 'cat' aparece solo una vez en la salida
print(animales) #imprime el contenido del conjunto 'animales'


#____________________________________

#crea un conjunto de números pares del 2 al 10
pares = {2, 4, 6, 8, 10}
#crea un conjunto de números grandes del 6 al 10
grandes = {6, 7, 8, 9, 10}

#resta: números grandes que NO son pares 
print(grandes - pares)

#unión: números que son grandes O pares 
print(grandes | pares)

#intersección: números que son grandes Y pares
print(grandes & pares)

#________________________________________________________

#imprime el conjunto 'animals' en su estado original los elementos aparecerán en orden aleatorio
print(animales)

#imprime una versión ordenada del conjunto 'animals', el resultado es una lista ordenada
print(sorted(animales))

#__________________________________________________________

#esto es un diccionario vacío
dicc_vacio = {}
print(dicc_vacio)
#esto es un conjunto vacío
conj_vacio = set()
print(conj_vacio)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#RANGES

#genera una lista con los enteros del 0 al 9 (10 no está incluido)
print(list(range(10))) 

#genera una lista del 1 al 10 
print(list(range(1, 11)))

#genera números impares entre 1 y 10, el tercer parámetro (2) define el incremento entre números
print(list(range(1, 11, 2)))

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#CONVERTING BETWEEN COLLECTION TYPES

#creación de una lista con elementos duplicados
animales_2 = ['cat', 'dog', 'goldfish', 'canary', 'cat']
print(animales_2)

#conversión a conjunto (set) para eliminar duplicados
animals_conjunto = set(animales_2)
print(animals_conjunto)

#conversión del conjunto a lista
animals_lista = list(animals_conjunto)  # Ejemplo: ['dog', 'cat', 'canary', 'goldfish']
print(animals_lista)

#conversión de la lista única a tupla
animals_tuple = tuple(animals_lista)  # Ejemplo: ('dog', 'cat', 'canary', 'goldfish')
print(animals_tuple)

#_______________________________________________________________-

#diccionario que mapea colores de canicas y sus cantidades
canicas = {"red": 34, "green": 30, "brown": 31, "yellow": 29}
print(canicas)

#extrae las claves (colores) y las convierte en lista
colours = list(canicas) 
print(colours)

#extrae los valores (cantidades) y los convierte en tupla
cantidad = tuple(canicas.values()) 
print(cantidad)

#convierte el diccionario "canicas" en un conjunto
canicas_conj = set(canicas.items())  
print(canicas_conj)

#________________________________________________

#creación de diccionario desde lista de tuplas
dicc1 = dict([(1, 2), (3, 4)])
print(dicc1)

#:::::::::::::::::::::::::::::::::::::::::::::::::::

#A BIT MORE ABOUT STRINGS

s = "abracadabra"  # Asignamos el string "abracadabra" a la variable s

#longitud del string
print(len(s))  

#posición del primer carácter 'b' de abracadabra 
print(s.index("b")) 

#acceso al primer carácter del string
print(s[0]) 

#parte del string desde posición 3 hasta 7 (7 no lo incluye)
print(s[3:7])

#los strings son inmutables esto daría error
#s[0] = "b"

#__________________________________________

#verificación de carácter en string
print('q' in 'abcd')  

#verificación de substring en string
print('cd' in 'abcd') 

#verificación de lista dentro de lista (no funciona en listas)
print(['a', 'b'] in ['a', 'b', 'c', 'd'])  

#________________________________________________


#lista de caracteres individuales
l = ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']

#une todos los elementos de la lista en un solo string sin espacios
s = "".join(l)
print(s)

#_____________________________________________________

#upla de nombres de animales
animals = ('cat', 'dog', 'fish')

#unión con espacios como separador
print(" ".join(animals))  # Resultado: "cat dog fish"

#unión con comas como separador
print(",".join(animals))  # Resultado: "cat,dog,fish"

#unión con coma y espacio como separador
print(", ".join(animals))  # Resultado: "cat, dog, fish"

#______________________________________________________

#divide el string usando los espacios como separador
print("cat    dog fish\n".split())  

#divide exactamente donde encuentra el caracter (|)
print("cat|dog|fish".split("|"))  

#divide cuando encuentra exactamente ", "
print("cat, dog, fish".split(", ")) 

#divide máximo 2 veces (resultando en 3 elementos)
print("cat, dog, fish".split(", ", 2))  

#::::::::::::::::::::::::::::::::::::::::::::::

#TWO DIMENSIONAL SEQUENCES

#matriz 4x3 (4 filas, 3 columnas) como lista de listas
matriz = [
    [1, 2, 3],    # Fila 0
    [4, 5, 6],    # Fila 1
    [7, 8, 9],    # Fila 2
    [10, 11, 12], # Fila 3
]

#acceso al elemento en la fila 0, columna 0
print(matriz[0][0])  

#las listas son mutables, por lo que podemos modificar elementos
matriz[0][0] = 42 

# Imprimimos la tabla completa para ver el cambio
print(matriz)

#___________________________________________________

#lista 2D donde cada sublista puede tener diferente longitud
lista2d = [
    [0],           # Fila 0 con 1 elemento
    [1, 2, 3, 4],  # Fila 1 con 4 elementos
    [5, 6],        # Fila 2 con 2 elementos
]
print(lista2d) 

#lista 3D (2x2x2)
lista3d = [
    [[1, 2], [3, 4]],  # Bloque 0
    [[5, 6], [7, 8]],  # Bloque 1
]

# Acceso al elemento en:
#primer bloque (índice 0)
#primera fila (índice 0)
#primera columna (índice 0)
print(lista3d)
print(lista3d[0][0][0])

#::::::::::::::::::::::::::::::::::::::::::::::

#LISTS OF LISTS AND SO FOR

#crea una lista con 100 ceros usando el operador de repetición *
lista_larga = [0] * 100
print(lista_larga) 

#crea una lista con 24 strings vacíos
dia = [""] * 24
print(dia)  

#crea 7 referencias a la lista dia
timetable = dia * 7
print(timetable) 

#crea 7 listas independientes de 24 strings vacíos cada una
timetable = [[""] * 24 for day in range(7)]
print(timetable) 
