# A list has 1 to 10. Make a new list that has [8, 6, 4, 2] in this specific order

# Execution point
int10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
int10.reverse() # Method to reverse the list
new_int10 = int10[2:9:2] # Sliced to take data FROM index 2 TO index 9 TAKING 2 STEPS
print(new_int10) # [8, 6, 4, 2]

# # Alt Approaches:
# # # just use -2 in steps instead of .reverse()
# # # just print instead of new list

# int10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(int10[7:0:-2]) # [8, 6, 4, 2]
