montuple = (3,"i",5,"wesh")
print(montuple[1])
for i in montuple:
    print(i)
if "wesh" in montuple:
    print ('L element wesh a bien ete trouve')

print(len(montuple))

montuple= montuple+("gros",)
print(montuple)
del montuple
