#Random Number Game by Pably

import random #importation of main libraries 

def run(): #main function
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = input('Elige un número del 1 al 100: ')
    numero_elegido = int(numero_elegido)
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numero_elegido = input('Elige otro numero: ')
        numero_elegido = int(numero_elegido)
    print('¡Ganaste!')


if __name__ == '__main__':
    run()