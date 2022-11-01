#Palindrome by Pably

def palindromo(palabra): #behavioral function
    palabra = palabra.replace(' ','') #borrar espacios
    palabra = palabra.lower() #minúscula todo
    palabra_inv = palabra[::-1] 
    if palabra == palabra_inv:
        return True
    else:
        return False


def run(): #main function
    palabra = input('Escribe una palabra: ')
    es_pal = palindromo(palabra)
    if es_pal == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')
        

if __name__ == '__main__':
    run()