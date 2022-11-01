#Primo Number by Pably

def es_primo(numero): #behavioral function
    contador = 0
    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % 1 == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

def run(): #main function
    numero = input('Escribe un numero: ')
    numero = int(numero)
    if es_primo(numero):
        print('Si es primo')
    else:
        print('No es primo')

if __name__ == '__main__':
    run()