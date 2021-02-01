from math import *

def module(a,b):
	resultat = (a**2 + b**2)**(1/2)
	return resultat


def argument(a,b):
	if (a == 0):
		if (b >= 0):
 			resultat = pi / 2 
		else:
			resultat = -pi / 2
	elif (a > 0):
		resultat = atan(b/a)
	else:
		if (b >=0):
			resultat = atan(b/a) + pi
		else:
			resultat = atan(b/a) - pi

