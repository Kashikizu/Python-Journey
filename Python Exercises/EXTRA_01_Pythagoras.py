# Find the hypotenuse using base and height

# Extra header
import math # Header to get sqrt()

# Execution point
# # int() typecasts the parameter into an integer
base = int(input("Enter the base ")) # We take value of base with input() and then convert it to number using int()
height = int(input("Enter the height "))

hypotenuse = math.sqrt((base**2) + (height**2)) # Using math header we use the math.sqrt() function to calculate the hypotenuse
# # Alt Approaches:
# # # Replacing math.sqrt with  (expression) ** (1/2)
# # # Replacing var**2 with     pow(var, 2)

print("Hypotenuse is", hypotenuse)

