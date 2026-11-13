#Dictionary Practice
Students={
    "name":"Anurag Pandey",
    "Age":35,
    "Language Teach":{
        "Java":"2hr",
        "C":"1hr",
        "Python":"1hr"
    },
    "List Have":[1,2,3,4,5],
    10:9,
    True:"Hello",
}

# Use of get method
# Syntax:- Dictionary.get(key,default)
# name=Students.get("name")
# print(name)
# print(Students.get("name"))

# print(Students.get("Hello"))
# print(Students.get("Income",0)) # get(key,default)

# use of keys,values,items
     #  keys methos return -class dict_keys
     #  value method return -class dict_values
     #  items method return -class dict_items

# keys_are=Students.keys()
# print(keys_are)
# print(f"Type return by keys-{type(keys_are)}")

# values_are=Students.values()
# print(values_are)
# print(type(values_are))

#use of items in for loop

# for key,value in Students.items():
#     print(f"Result of items method-{key,":",value}")

# use of update
# Syntax dictionary.upadte({other_dict})
Students.update({"name":"Aarya Pandey","marks":90})
print(Students["marks"])




