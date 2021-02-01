Tcelsius=float(input("entrez la temperature en degres celsius: "))
Tfahrenheit=(Tcelsius*1.8)+32
print("Une temperature de " +str(Tcelsius)+" degres celsius correspond a "+str(Tfahrenheit)+" degres fahrenheit.")

#Correction

def Tfahrenheit(Tcelsius): 
	resultat = 9/5 * Tcelsius + 32
	return(resultat)
