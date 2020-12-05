x=int(input())
a=x
if x==0:
	x=1
if x<0:
	x=0
while a>1:
	x=x*(a-1)
	a=a-1
print(x)
