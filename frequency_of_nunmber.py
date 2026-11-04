l=[2,4,3,2,5,5,4,2,1]
fre=[]
for item in l:
    if item not in fre:
        count=0
    for x in l:
        if x==item:
            count+=1
    print(f"{item} appear {count}")
    fre.append(item)    

