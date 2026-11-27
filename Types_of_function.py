# Four type of function in python...
# Type 1 function- no parameter,no return type
def sum():
     a=int(input("Enter a number\n"))
     b=int(input("Enter one more number\n"))
     print(a+b,end='\n')
sum()

# Type 2 function- with parameter, without return type
def sum(a,b):
    print(a+b,end='\n')

a=int(input("Enter a number\n"))
b=int(input("Enter one more number\n"))
sum(a,b)

#Type 3 No parameter ,with return
def sum():
    a=int(input("Enter a number\n"))
    b=int(input("Enter one more number\n"))
    return a+b

print(sum(),end='\n')

#Type 4 With Parameter,with return

def sum(a,b):
    return a+b

a=int(input("Enter a number\n"))
b=int(input("Enter one more number\n"))
print(sum(a,b),end='\n')
    
