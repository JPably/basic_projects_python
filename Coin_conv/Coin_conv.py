#Coin Conversor by Pably

def conversor(tipo_pesos, valor_dolar): #main function
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos) 
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)

    print("Tienes $" + dolares + " USD")
    

menu = """
Welcome to the coin conversor 💸

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = input(menu)
opcion = int(opcion)

if opcion == 1:
    conversor("colombianos", 4307.46)
    
elif opcion == 2:
    conversor("argentinos", 132.13)

elif opcion == 3:
    conversor("mexicanos", 20.75)

else:
    print('ERROR. Ingresa una opción valida, por favor 😢')
