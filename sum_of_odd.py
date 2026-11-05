list=[]
print("Enter 10 integer type values in list")
i=0

while i<10:
    val=int(input())
    list.append(val)
    i+=1

# find odd values from list and sum them
sum=0
i=0 #for iteration
while i<len(list):
    if list[i]%2!=0:
        sum=sum+list[i]
    i=i+1
print(f"Total Sum of given list is {sum}")

