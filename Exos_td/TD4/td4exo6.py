def superstar(N,Plein):
	if N==1:
		print("*")
	elif N <= 1:
		print("")
	elif Plein==True:
		print(N*"*")
	else:
		print("*",((N-2)*(" ")),"*")
superstar(-2,False)
