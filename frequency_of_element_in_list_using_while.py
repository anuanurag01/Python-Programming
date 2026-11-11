#In this program i am going to check frequency of each element in given List.
# Step 1- Take number from user to create a list
# Step 2- take another list with same length of list that have numbers
# 

numbers=[]
i=0
while i<7:
    val=int(input("Enter a value\n"))
    numbers.append(val)
    i+=1

print("Entered value in list are:-\n")
i=0
while i<7:
    print(numbers[i],end="\t") # end ="\t" is used for one tab space while printing numbers
    i+=1
print()

# Logic to check frequency of each number
i=0
frequency=[0]*len(numbers)
while i<len(numbers):
    if frequency[i]==1:
        i=i+1
        continue
    count=1
    j=i+1
    while j<len(numbers):
        if(numbers[j]==numbers[i]):
            count+=1
            frequency[j]=1
        j=j+1
   
    print(f"{numbers[i]} count is {count}")
    i=i+1
    


