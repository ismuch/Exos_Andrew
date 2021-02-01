x = input("Choix ")
if x == "a":
    somme=0
    n=int(input("Entrez un entier:\n"))
    b=n
    while n>0:
        n=n-1
        somme=somme+n
    print(somme)

    s=b*(b-1)/2
    print(s)

    if s==somme:
        print("resultats identiques")
    print(s==somme)
elif x=="b":
    fact = 1
    n = int(input("Entrez un entier\t"))
    for i in range(1, n + 1):
        fact = fact * i
    print("resultat de la factorielle de", n, "est", fact)

elif x=="A" or x=="B":
    print ("Veuillez taper votre choix en miniscule")

else:
    print ("Choix non valide")