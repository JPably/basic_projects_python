#Age Detector by Pably

edad = input("escribe tu edad: ")
edad = int(edad)
if edad > 17:
    print('Eres mayor de edad')
else: #Si no...
    print('Eres menor de edad')

numero = input("Escribe un número: ")
numero = int(numero)

if numero > 5:
    print('Es mayor a 5')
elif numero == 5: #también si...
    print('Es igual a 5')
else: #Si no...
    print('Es menor a 5')