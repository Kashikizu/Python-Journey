# A function takes a string and number. It 
# - prints the string the specified number of times
# - capitalizes every letter
# - if the number is more than 10 it says you are too loud once (and nothing else)
# - returns "done"
# - must have default values

# Function point

def shouter(shout = "AYAYA?", num = 3):
    if(num >= 10):
        print("You are too loud")
    else:
        while(num > 0):
            print(shout.upper())
            num -= 1
    return "done"


# Execution point

print(shouter()) # To check default value
print(shouter("AYAYA!", 5)) # To check <10 condition
print(shouter("AYAYA!", 15)) # To check You are too loud


# # Alt Approaches:
# # # Replace while loop with for i in range(num) 