"""
Ejercicio Python: Condicionales Tipo impositivo declaración de Renta

Los tramos impositivos de un país en concreto son los que figuran en la siguiente tabla:

Menos de 12000€ 7%
Entre 12000€ y 18000€ 15%
Entre 18000€ y 35000€ 21%
Entre 35000€ y 70000€ 35%
Más de 70000€ 45%


Crea un programa que pregunte por consola la renta. En función de la renta introducida, el programa 
devolverá el texto: “A la renta (aquí iría la renta introducida) le corresponde un (aquí iría el tipo impositivo) de tipo impositivo.

Ejemplo: En caso de introducir por consola 13500, el programa devolverá el texto: “A la renta 13500 le corresponde un 15% de tipo impositivo”

El programa debe permitir la introducción de rentas decimales.

"""

print("Ejercicio tipo impositivo declaración de renta")

renta = float(input("Por favor introduzca su renta: "))

if renta<12000:
    print("A la renta de " + str(renta) + " le corresponde un 7% de tipo impositivo")

elif renta<18000:
    print("A la renta de " + str(renta) + " le corresponde un 15% de tipo impositivo")

elif renta<35000:
    print("A la renta de " + str(renta) + " le corresponde un 21% de tipo impositivo")

elif renta<70000:
    print("A la renta de " + str(renta) + " le corresponde un 35% de tipo impositivo")
 
else:
    print("A la renta de " + str(renta) + " le corresponde un 45% de tipo impositivo")


print("programa cálculo tipo impositivo de renta hecho por el profesor")

renta = float(input("Introduce la renta anual del 2020: "))

if renta<12000:
    tipo = 7
elif renta<18000:
    tipo = 15
elif renta<35000:
    tipo = 21
elif renta<70000:
    tipo = 35
else:
    tipo = 45

print("A la renta de " + str(renta) + " le corresponde un " + str(tipo) + "% de tipo impositivo")
