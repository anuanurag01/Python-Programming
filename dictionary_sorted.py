marks={
    "anurag":80,
    "sanjay":90,
    "rajesh":100,
    "abhinav":95
}

sorted_keys=sorted(marks) # this will return list of keys in sorted order
print(sorted_keys)
sorted_values=sorted(marks.values())
# this will return list of values in sorted order
print(sorted_values)
# this will return tuple of sorted keys but with their values
sorted_keys_in_pair=sorted(marks.items())

print(sorted_keys_in_pair)

# sorted values in pair

sorted_values_in_pair=sorted(marks.items(),key=lambda x:x[1],reverse=True)
print(sorted_values_in_pair)
