# 1- Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("\nEjercicio1");
print("-----------\n");

print("Hola Mundo!");

# 2- Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#    el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#    por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#    realizar la impresión por pantalla.

print("\nEjercicio2");
print("-----------\n");

nombre= input("Ingrese su nombre: ");

print(f"\nHola {nombre}!");

# 3- Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#    imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#    “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#     años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#     la impresión por pantalla.

print("\nEjercicio3");
print("-----------\n");

nombre= input("Ingrese su nombre: "); # Preguntar si se puede pedir que el usuario ingrese todos los datos en 1 línea.
apellido= input("Ingrese su apellido: ");
edad = int(input("Ingrese su edad: "));
lugar_residencia= input("Ingrese su lugar de residencia: ");

print(f"\nSoy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.");

# 4- Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

print("\nEjercicio4");
print("-----------\n");

radio= int(input("Ingrese el radio del círculo: ")); # Puede ser entero o real.

area= (3.14159 * (radio * radio));
perimetro= (2*(3.14159)*radio);

print(f"\nEl área del círculo es {area} m2 y el perímetro es {perimetro} m.");

# 5- Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

print("\nEjercicio5");
print("-----------\n");

segundos= int(input("Ingrese una cantidad de segundos: "));

horas= (segundos/3600);

print(f"\n{segundos} s equivalen a {horas} hr.");

# 6- Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#    multiplicar de dicho número.

print("\nEjercicio6");
print("-----------\n");

numero= int(input("Ingrese un numero: "));

i=0;

while i<= 10:

    print(f"{numero} x {i} = ",(numero*i));
    i = i +1;

# 7- Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#    pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("\nEjercicio7");
print("-----------\n");

numero_1= int(input("Ingrese un número entero distinto de 0: "));
numero_2= int(input("Ingrese otro número entero distinto de 0: "));


print(f"\n{numero_1} + {numero_2} = ",(numero_1+numero_2));
print(f"{numero_1} - {numero_2} = ",(numero_1-numero_2));
print(f"{numero_1} * {numero_2} = ",(numero_1*numero_2));

if numero_2 !=0 :
    print(f"{numero_1} / {numero_2} = ",(numero_1/numero_2)); 
else:
    print("No se puede dividir por 0. Ingrese otro valor.");

# 8- Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#    de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#    modo: IMC = peso en Kg / (altura en M)2.

print("\nEjercicio8");
print("-----------\n");

altura= float(input("Ingrese su altura: "));
peso= float(input("Ingrese su peso: "));

print("\nSu IMC es: "+ str(peso/(altura*altura))+ " Kg/M2.");

# 9- Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#    pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#    Temperatura en Fahrenheit = 9/5 . Temperatura en Celsius + 32.

print("\nEjercicio9");
print("-----------\n");

temperatura_celsius= float(input("Ingrese  una temperatura en grados Celsius: "));

print(f"\n{temperatura_celsius} grados Celsius equivale a "+ str((temperatura_celsius * (9/5))+32) + " grados Fahrenheit.");

# ) 10- Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#       dichos números.


print("\nEjercicio10");
print("-----------\n");

numero_1= int(input("Ingrese el primer número: "));
numero_2= int(input("Ingrese el segundo número: "));
numero_3= int(input("Ingrese el tercer número: "));

print("\nEl promedio es: ", ((numero_1+numero_2+numero_3)/3));