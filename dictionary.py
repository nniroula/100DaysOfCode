#!/Users/nabinniroula/anaconda3/bin/python

# create python dictionary
dict = {}

# key value pair is first define the key and then value
# dict[key] = value
dict["name"] = "nabin"
#print(dict)

# create a dictionary and access its keys and values separately

dict2 = {}
dict2["name"] = "Nabisha"
dict2["College"] = "Will decide in future"
dict2["Gender"] = "femal"
dict2["age"] = "2 months"
dict2["year born"] = 2021

# print(dict2)

# access its keys
print("The keys in dict2 are: ")
for val in dict2:
    print(val)

# access its values for keys
print("The values for keys in dict2 are: ")
for value in dict2:
    print(dict2[value])
