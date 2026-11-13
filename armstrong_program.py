#armstrong number of any digit
#num=int(input("Enter a number"))
for num in range(100000):
    count=0
    temp=num
    while temp>0:
        count+=1
        temp=temp//10
# print(f"{num} is {count} digit number")
# print(f"value of temp variable{temp}")

    temp=num
    sum=0
    rem=0
    power=0
    while temp>0:
        rem=temp%10
        power=rem**count
        sum=sum+power
        temp=temp//10

    if(num==sum):
        print(f"{num} is a armstrong number")
