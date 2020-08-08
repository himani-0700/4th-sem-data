l=[10,20,20,30,30,30,40,50,50,50,50]
for x in range(1,len(l)):
    if l[x] == l[x-1]:
        l.pop(x)
print(l)
