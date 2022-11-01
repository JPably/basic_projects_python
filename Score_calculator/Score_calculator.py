#Score Calculator by Pably

def notas():

    nota1 = input("¿Nota corte 1?: ") #note 1
    nota1 = float(nota1)
    nota1 = round(nota1, 2)
    porc1 = input("¿A cuánto % equivale?: ")
    porc1 = float(porc1)

    nota2 = input("¿Nota corte 2: ") #note 2
    nota2 = float(nota2)
    nota2 = round(nota2, 2)
    porc2 = input("¿A cuánto % equivale?: ")
    porc2 = float(porc2)

    nota3 = input("¿Nota corte 3: ") #note 3
    nota3 = float(nota3)
    nota3 = round(nota3, 2) 
    porc3 = input("¿A cuánto % equivale?: ")
    porc3 = float(porc3)

    nota4 = input("¿Nota corte 4: ") #note 4
    nota4 = float(nota4)
    nota4 = round(nota4, 2)
    porc4 = input("¿A cuánto % equivale?: ")
    porc4 = float(porc4)

    nota5 = input("¿Nota corte de las P.O: ") #note 5
    nota5 = float(nota5)
    nota5 = round(nota5, 2)
    porc5 = input("¿A cuánto % equivale?: ")
    porc5 = float(porc5)

    notafinal = (nota1 * porc1) + (nota2 * porc2) + (nota3 * porc3) + (nota4 * porc4) + (nota5 * porc5) #final note

    if notafinal >= 60:
            print("Pasaste la unidad con ", notafinal)
    else:
            print("Perdiste la unidad con ", notafinal)


if __name__ == '__main__':
    notas()

