# A list has 1 to 5. If value is 2, print its 2, else print its not 2 and if value is 5 print the last item 6 times

# Execution point
ex_list = [1, 2, 3, 4, 5]
for x in ex_list:
    if (x == 2):
        print("The value is 2")
    elif (x == 5):
        counter = 6
        while(counter > 0):
            print("Last Item")
            counter -= 1
    else:
        print("The value is not 2")
        
# # Alt Approaches:
# # # The elif can just be put at the very end WITHOUT elif