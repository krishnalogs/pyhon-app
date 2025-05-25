# Dictionary
# it is a key value pair
# where key can be string, int, float, only primitive
# where c=value can be lists, tuple, dictionary, both primitive and non-primitive

d1 = {"name" : "mohan"} 
# print(d1["name"])
# print(d1.values())
# print(d1.items())

# for loop using items
# for x,y in d1.items():
#     print(x, "-->", y)

# for loop using keys
# for i in d1.keys():
#     print(i, "-->", d1[i])

# for i in d1.keys():
#     print(i)

# d1["age"] = 24
# d1["interests"] = ["exploring places", "trekking", "movies", "songs", "guitar"]
# d1["skills"] = {"cloud": ["aws","google"], "prog" : ["shell", "python"], "servicenow" : "yes"}
# print(d1)

# print(d1["skills"])
# print(d1["skills"]["cloud"])

dict1 = {"key1":1, "key2":2}
dict2 = {"key2":2, "key1":1}
# if key and value is equal then will be true, as the sequence of the elements doesnot matter, key value pair order also doesn't matter.
print (dict1 == dict2) 


