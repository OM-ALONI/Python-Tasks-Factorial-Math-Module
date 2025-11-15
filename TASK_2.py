import math

# Ask user for input
num = float(input("Enter a number: "))

# Calculations using math module
square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

# Display results
print("Square root of", num, ":", square_root)
print("Natural logarithm (log base e) of", num, ":", natural_log)
print("Sine of", num, "in radians :", sine_value)
