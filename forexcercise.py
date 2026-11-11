# built-in-function range- range(stop) or range(start,stop,step)


n=int(input("enter stop value for range function\n"))
sequence=range(n)# range(stop)

for x in sequence:
    print(x,end=" ")

seq=range(11,21)
for y in seq:
    print(y,end=" ")

seq=range(2,20,2)
for v in seq:
    print(v,end=" ")

seq=range(20,-10,-3)
for h in seq:
    print(h,end="\t")
print()
seq=range(0,30,5)
for j in seq:
    print(j,end="\t")

list=[]

seq=range(0,10,2)
for x in seq:
    list.append(x)
print(list)

list=[]
for u in range(5,15,1):
    list.append(u)
print(list)

tup=(0,0,0,0,0)
seq=range(5)
for j in seq:
    tup[j]=j # this line will give error
print(tup)

