"""

La raíz cuadrada de un número negativo no puede hallarse, así que vamos a crear un programa que halle la raíz de un número positivo
y cuando el estudiante ponga un número negativo le vamos a decir que está errado y se le dará 3 intentos más, para lo que usaremos
la instrucción break, para romper el bucle al tercer intento.

Se importará el múdulo math para poder hacer cálculos matemáticos.
"""
import math
print("Este programa halla la raíz cuadrada de un valor numérico")
numero = int(input("Por favor introduce un número: "))

intentos = 1 # Variable contador, para contar el número de intentos, se inicializa en 1

while numero<0: # Mientras que la variable número sea negativa imprima el siguiente mensaje
    print("Disculpa tienes un error, vuelve a intentar")
    numero = int(input("Por favor introduce un número: ")) # Ingresar otro número en consola
    intentos = intentos+1  #esta variable cuenta el número de intentos
    if intentos==3: #si los intentos son 3, salga del bucle
        break

if intentos==3 and numero<0: #si los intentos son 3 y la variable número es negativa, imprima el siguiente mensaje
    print("Lo siento, no puedo hacer el cálculo, el valor numérico no puede ser negativo")
    
else: 
    #para todo lo demás realice el cálculo de la raíz cuadrada
    print("La raíz cuadrada de " + str(numero) + " es: " + str(math.isqrt(numero)))
