def superstar(N,Plein):
        if N==1:
                print("*")
        elif N <= 1:
                print("")
        elif Plein==True:
	somme=0
	for i in range(N):
		print((i)*"*")
        print(N*"*")
        else:
                print("*",((N-2)*(" ")),"*")

superstar(5,True)

