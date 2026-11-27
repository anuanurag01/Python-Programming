#return gift from function

def check_number(n):
    if(n<0):
        return "negative"
    else:
        return "positive"

message_From_function=check_number(-2)
print(message_From_function)

# Python can return multiple values

def min_max(L):
    return min(L),max(L) # function return multiple values in form of tuple

minimum_value,maximum_value=min_max([4,231,1]) # here i am unpacking tuple which is returned from function
print(minimum_value,maximum_value,sep="::",end="\n")
