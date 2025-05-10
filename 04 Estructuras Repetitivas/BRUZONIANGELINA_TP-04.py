# TP-04: Estructura repetitivas
# Ejercicio 1
print("\n1-Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100", end="\n")
print("incluyendo ambos extremos), en orden creciente, mostrando un número por línea.\n") 

# Iteramos en orden creciente desde 0 hasta 100 (Incluyendo ambos extremos).
# Mostramos cada numero entero comprendido entre ellos.
for num in range(101): 
    print(num)                

# Ejercicio 2
print("\n2-Desarrolla un programa que solicite al usuario un número entero y ", end="\n")
print("y determine la cantidad de dígitos que contiene.\n") 

# Inicializamos el contador en 0.
cont = 0

# Solicitamos al usuario que ingrese un número entero.
num = input("Ingrese un número entero: ") # Ver como verificar una entrada no valida

# Solicitamos que vuelva a ingresar un número entero mientas num no sea digito.
while not num.isdigit():
    num = input("Ingreso incorrecto. Ingrese un número entero: ")

# Convertimos el número ingresado a entero y lo hacemos positivo.
num = abs(int(num)) 

# Verificamos si el número es 0.
# En dicho caso, inicializamos el contador en 1.
if num == 0 :
    cont = 1
   
# Mientras num sea diferente a 0, dividiremos a num por 10
# hasta llegar a 0 e iremos contando dichas divisiones que corresponden a cada dígito.
while num != 0:
    num = num //10 #Con números negativos, el redondeo hacia abajo se traduce en redondear hacia el número entero más pequeño (hacia el infinito negativo)
    cont += 1


# Nostramos la cantidad de dígitos del número ingresado.
print(f"La cantidad de dígitos del número ingresado es: {cont}\n")

# Ejercicio 3
print("\n3-Escribe un programa que sume todos los números enteros comprendidos", end="\n")
print("entre dos valores dados por el usuario, excluyendo esos dos valores.\n") 

# Inicializamos la  variable suma en 0.
suma = 0

# Solicitamos al usuario que ingrese 2 números enteros.
num1 = input("Ingrese el primer número entero: ") 

# Solicitamos que vuelva a ingresar un número entero mientas num1 no sea digito.
while not num1.lstrip("+-").isdigit():
    num1 = input("Ingreso incorrecto. Ingrese nuevamente el número entero: ")

num2 = input("Ingrese el segundo número entero: ")

# Solicitamos que vuelva a ingresar un número entero mientas num2 no sea digito.
while not num2.lstrip("+-").isdigit():
    num2 = input("Ingreso incorrecto. Ingrese nuevamente el número entero: ")

# Convertimos num1, num2 a entero y los hacemos positivos.
num1 = int(num1)
num2 = int(num2)

if num1 > num2:
    for num  in range(num2 +  1, num1):
        suma += num 

else: 
    for num  in range(num1 +  1, num2):
        suma += num   
       

# Mostramos la suma de los números enteros comprendidos entre num1 y num2.
print(f"La suma de los valores enteros comprendidos entre {num1} y {num2} es: {suma}\n")

# Ejercicio 4
print("\n4-Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia.", end="\n")
print("El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0..\n")

try:

    suma = 0

    num = int(input("Ingrese un número entero (0 para finalizar): "))

    while num != 0:
        suma += num
        num = int(input("Ingrese un número entero (0 para finalizar): "))

    print("El total acumulado es :  ", suma)

except Exception:
    print("Ingreso incorrecto. Debe ingresar un número entero.")

# Ejercicio 5
print("\n5-Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9", end="\n")
print("Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.\n")

import random

# Inicializamos el contador de intentos en 0.
intentos = 0    
# Generamos un número aleatorio entre 0 y 9.
num_aleatorio = random.randint(0, 9)
# Solicitamos al usuario que adivine el número.
num = int(input("Adivina el número entre 0 y 9: "))

# Mientras el número ingresado por el usuario sea diferente al número aleatorio,
# incrementamos el contador de intentos y solicitamos un nuevo número.  
while num != num_aleatorio:
    intentos += 1
    if num < num_aleatorio:
        print("El número es mayor. Intenta nuevamente.")
    else:
        print("El número es menor. Intenta nuevamente.")
    num = int(input("Adivina el número entre 0 y 9: "))
# Incrementamos el contador de intentos para contar el último intento exitoso.
intentos += 1   
# Mostramos el número aleatorio y la cantidad de intentos necesarios para acertar.
print(f"El número aleatorio era: {num_aleatorio}")      
print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.\n")

# Ejercicio 6
print("\n6-Desarrolla un programa que imprima en pantalla todos los números pares", end="\n")
print("comprendidos entre 0 y 100, en orden decreciente..\n")

for  num in range(100, -1, -1):   
    if num % 2 == 0 :
        print(num) 

# Ejercicio 7
print("\n7-Crea un programa que calcule la suma de todos los números comprendidos entre 0", end="\n")
print("y un número entero positivo indicado por el usuario.\n")

try:
    num = int(input("Ingrese un entero positivo: "))

    while num < 0:
        num = int(input("Ingreso incorrecto. Ingrese un entero positivo: "))

    suma = 0
    for num in range(num +1):
        suma += num

    print(f"La suma comprendida ente 0 y {num} es: {suma}\n")

except Exception:
    print("Ingreso incorrecto. Debe ingresar un número entero positivo.")

# Ejercicio 8
print("\n8-Escribe un programa que permita al usuario ingresar 100 números enteros.", end="\n")
print("\n  Luego, el programa debe indicar cuántos de estos números son pares,", end="\n")
print("\n  cuántos son impares, cuántos son negativos y cuántos son positivos.", end="\n")
print("\n  (Nota: para probar el programa puedes usar una cantidad menor,", end="\n")
print("\n  pero debe estar preparado para procesar 100 números con un solo cambio).")

try:
    par = 0
    impar = 0
    positivo = 0
    negativo = 0

  
    for i  in range(1, 101):
        num = int(input("\nIngrese un número entero: "))
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
        
        if num > 0:
            positivo += 1
        elif num < 0:
            negativo += 1
       

    print(f"\nCantidad de números pares: {par}")
    print(f"Cantidad de números impares: {impar}")
    print(f"Cantidad de números positivos: {positivo}")
    print(f"Cantidad de números negativos: {negativo}")

except Exception:
    print("Ingreso incorrecto. Debe ingresar un número entero.")

# Ejercicio 9
print("\n9-Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.", end="\n")
print(" (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).\n")

try:
    cont = 0
    suma = 0
    media = 0

    for i  in range(1,101):
        num = int(input("\nIngrese un número entero: "))
        suma += num
        cont += 1

    media = suma / cont
    print(f"\nLa media de los números ingresados es: {media}\n")

except Exception:
    print("Ingreso incorrecto. Debe ingresar un número entero.")

# Ejercicio 10
print("\n9-Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.", end="\n")
print(" Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.\n")
try:
    num = input("Ingrese un número entero: ")

    # Verificamos si el número ingresado es un dígito.
    while not num.lstrip("+-").isdigit():
        num = input("Ingreso incorrecto. Ingrese un número entero: ")

    # Convertimos el número ingresado a entero.
    num = abs(int(num))

    # Convertimos el número a cadena y lo invertimos.
    num_invertido = str(num)[::-1]

    # Mostramos el número invertido.
    print(f"El número invertido es: {num_invertido}\n")

except Exception:
    print("Ingreso incorrecto. Debe ingresar un número entero.")
