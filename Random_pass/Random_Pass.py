#Random Password by Pably

import random #importation of main libraries 

def generar_password(): #behavioral function

    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    simb = ['!', '#', '$', '%', '&', '/', '(', ')', '=', '?', '¡', '¿']
    nume = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caract = mayus + minus + simb + nume

    password = []

    for i in range(18): #my loop is for 18 random characters of my variables 
        caract_random = random.choice(caract)
        password.append(caract_random)
    
    password = ''.join(password)
    return password


def run(): #main function
    password = generar_password()
    print('Tu nueva contraseña es: ' + password)


if __name__ == '__main__':
    run()

