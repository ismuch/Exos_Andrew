n = int(input("entrez un entier superieur a un:\t"))
if n > 1:
	for n in range(n,0,-3):
		print(n,n-1,n-2)
else:
	print("erreur entrez un entier superieur a un")
