# Execution point

# # Tuples: Tuples cannot be changed
example_tuple = (1, 2, 3, "This is a tuple")
print(example_tuple) # (1, 2, 3, 'This is a tuple')
print(example_tuple[0], example_tuple[-1]) # 1 This is a tuple


# # Lists:
example_list = [1, 2, 3, "This is a list"]
print(example_list) # [1, 2, 3, 'This is a list']
print(example_list[1], example_list[-2]) # 2 3


# # # List Stuffs:
example_list.append("This is appended in the list")
print(example_list) # [1, 2, 3, 'This is a list', 'This is appended in the list']

example_tuple2 = (1, 2, 3, "This is another tuple")
print(example_tuple2) # (1, 2, 3, 'This is another tuple')
example_tuple2 = list(example_tuple2)
print(example_tuple2) # [1, 2, 3, 'This is another tuple']



# # Sets: Keeps unique values
example_set = {1, 2, 3, "This is a set"}
print(example_set) # {1, 2, 3, 'This is a set'}
# # print(example_set[0], example_set[1]) will not work

# # # Set Stuffs:
example_list2 = [1, 1, 2, 3]
print(example_list2) # [1, 1, 2, 3,]
example_list2 = set(example_list2) # Making the list into a set. This will replace all the duplicate values
print(example_list2) # {1, 2, 3}



# # Dictionaries: Key:Value pairs
example_dictionary = {1:2, 3:4, "cont":"This is a dictionary"}
print(example_dictionary) # {1: 2, 3: 4, 'cont': 'This is a dictionary'}
print(example_dictionary[1], example_dictionary["cont"]) # 2 This is a dictionary

# # # Dictionary Stuffs:
example_dictionary["appended"] = "This is added later"
print(example_dictionary) # {1: 2, 3: 4, 'cont': 'This is a dictionary', 'appended': 'This is added later'}
print(example_dictionary["appended"]) # This is added later



# # # Slicing:
print(example_tuple[0:3]) # (1, 2, 3)
print(example_list[0:3]) # [1, 2, 3]