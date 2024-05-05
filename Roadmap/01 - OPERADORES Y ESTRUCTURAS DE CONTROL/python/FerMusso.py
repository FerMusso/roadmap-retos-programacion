'''
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
'''
#operadores aritméticos
suma = 45 + 38
print(f"suma: 45 + 38 = {45 + 38}")  #interpolado con cadena de texto
print(suma) #impreso directamente sin cadena de texto
print(f"resta: 45 - 38 = {45 - 38}")
print(f"multiplicación: 45 * 38 = {45 * 38}")
print(f"división: 45 / 38 = {45 / 38}")
print(f"división entera: 45 // 38 = {45 // 38}")
print(f"módulo: 45 % 38 = {45 % 38}")
print(f"potencia: 45 ** 38 = {45 ** 38}")

#operadores de comparación (pueden comparar tanto números como variables, a modo didáctico aquí sólo se comparan números)
print(f"igualdad: 10 es = a 3? = {10 == 3}")  #false
print(f"desigualdad: 10 es distinto de 3? = {10 != 3}")  #true
print(f"mayor que: 10 > 3 = {10 > 3}")  #true
print(f"menor que: 10 < 3 = {10 < 3}")  #false
print(f"mayor igual que: 10 >= 3 = {10 >= 10}")  #true
print(f"menor igual que: 10 <= 3 = {10 <= 14}")  #false

#operadores lógicos

print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}") #true
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 8 es {10 + 3 == 13 or 5 - 1 == 8}") #true (xq al menos una debe ser verdadera)
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}") #true (ya que la condición no se cumple)

#operadores de asignación
my_number = 11 # asignación
print(my_number)

my_number += 1 #suma y asignación - puede ser "my_number + 1" también
print(my_number) 
my_number -= 1 #resta y asignación
print(my_number) 
my_number *= 1 #multiplicación y asignación
print(my_number) 
my_number /= 1 #división y asignación
print(my_number) 
my_number %= 1 #módulo y asignación
print(my_number) 
my_number **= 1 #exponente y asignación
print(my_number) 
my_number //= 1 #división entera y asignación
print(my_number)   # etc...

# operadores de identidad (valor de la posición de memoria, no de la variable...)
# ejemplo, el operador "is":
my_number = 1.0
my_new_number = 1.0
print (f"my_new_number is my_number es {my_new_number is my_number}") # =>da "false" por màs que tenga el mismo valor, porque no
# compara los valores en sí de la variable, sino la DIRECCIÓN DE MEMORIA de esas variables. Para que de true debemos hacer:
my_new_number = my_number #así le asigna el mismo lugar de memoria
print (f"my_new_number is my_number es {my_new_number is my_number}") #true
#operador "is not":
print (f"my_new_number is not my_number es {my_new_number is not my_number}") #false (porque sí son iguales ahora

# operadores de pertenencia
print(f"'a' en 'fernando' = {'a' in 'fernando'}") #true
print(f"'u' en 'fernando' = {'u' not in 'fernando'}") #true

# operadores de bit (poco usados)

a = 10 # en binario 1010
b = 3 #  "      "   0011
print(f"AND: 10 & 3 = {10 & 3}") # da igual a 2, que es lo que da en binario de comparar los correspondientes bits de 10 y 3
''' Así, solo 1 con uno da uno, lo demas da 0, por ello comparando bit a bit:
                      1010
                      0011
                      -----
                      0010  = es 2 en binario
'''
# otros operadores binarios:
print(f"OR: 10 | 3 = {10 | 3}") # igual a 1011 (11) xq compara cada bit y si al menos uno de ellos es =1, el resultante es 1. 
                                # de lo contrario es 0.
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # igual a 1001 (9), ya que si los bits son diferentes el resultado es 1.
print(f"NOT: ~10 = {~10}") # igual a-11, intercambia el valor bit a bit de cada elemento.
print(f"desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010 desplaza dos lugares los bit agregando ceros a 
#la izquierda (?)y da 2 binario, o sea de 1010 a 0010.
print(f"desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000

'''
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructura
de control que existan en tu lenguaje: Condicionales, iterativas, excepciones...
'''

# condicionales:

my_string = "fernando"

if my_string == "fernando":
  print("my_string es 'fernando'")
elif my_string == "brais":
  print("my_string es 'fernando'")
else:
  print("my_string no es 'fernando' ni 'brais'")

# iterativas

#for --->  para estructuras que tienen más de un elemento o para ejecutar una acción varias veces (bucles)

for i in range(11):
  print(i) #imprime 11 números, del 0 al 10

# while ----> el bucle se ejecuta mientras esa condición sea verdadera

i = 0

while i <= 10:
  print(i) # imprime 0 infinitas veces ya que nunca se cumple 1 > a 10, pero le puedo sumar 1 hasta llegar a 11 y parar:
i += 1

# manejo de excepciones

#supongamos ==> print(10 / 0)  esto colapsaría el código, para eso se usa el try 'catch'

try:
  print(10/0)
except: #este es el 'catch' en python
  print("se ha producido un error")
finally: #haya o no errores se ejecuta al final en cada manejo de errores
  print("ha finalizado el manejo de excepciones")

#dificutad extra: imprimir nº entre 10 y 55, pares, sin el 16 ni los múltiplos de 3.

for number in range(10, 56):
  if number % 2 == 0 and numbrer != 16 and number % 3 != 0:  
    #identifico los pares sabiendo que el módulo de ellos da 0 y es distinto de 0 para los multiplos de 3 
  print(number)
