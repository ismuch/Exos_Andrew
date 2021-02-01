montuple = (3,"janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre")
x=int(input("Choisissez un chiffre de 1 a 12 : "))
if 0<x<13:
    print(x, "correspond au mois de",montuple[x])
else:
    print("erreur - vous devez entrer un entier de 1 a 12")