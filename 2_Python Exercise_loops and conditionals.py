
"""
Ejercicio Python: Diccionarios y Listas 

Elaborar un programa que genere un número aleatorio entre 1 y 100. Para ello
debemos importar el módulo random y utilizar la instrucción random.randint(1,100). Esta
instrucción genera un número entero entre 1 y 100.

A continuación, se le pide al usuario que introduzca un número por consola entre 1 y 100. Si el
número introducido por el usuario es menor, se imprime en consola un mensaje indicando que
el número aleatorio es mayor que el introducido por él. Si el número introducido por el usuario
es mayor que el aleatorio, se imprime un mensaje indicando que el número aleatorio es menor
que el introducido por él. Después de indicar si es mayor o menor, se vuelve a pedir al usuario
que introduzca un número entre 1 y 100.

Finalmente, se debe averiguar cuál es el número aleatorio generado por el programa a base de ir
aproximándonos intento tras intento, y hacerlo en el menor número de intentos posibles así que
también debemos controlar cuántos intentos consume el usuario para adivinar el número
aleatorio generado por el programa.

Cuando el usuario encuentre finalmente el número aleatorio, el programa imprimirá en consola
“Correcto. Has utilizado…” y el nº de intentos consumidos.

"""

import random

aleatorio = random.randint(1,100)
#print(aleatorio)
numero = int(input("Por favor introduce un número entre 1 y 100: "))
intentos = 1

while numero != aleatorio:
    if numero < aleatorio:
        print("El número aleatorio es mayor que el introducido por usted")
    else:
        print("El número aleatorio es menor que el introducido por usted")

    numero = int(input("Por favor introduce un número entre 1 y 100: "))
    intentos = intentos + 1
    if intentos == 7:
        break

if intentos <= 7 and numero==aleatorio:
    print("¡Correcto! Has utilizado " + str(intentos) + " intentos")
else:
    print("El número introducido por usted es diferente al número aleatorio que fue: " + str(aleatorio))
