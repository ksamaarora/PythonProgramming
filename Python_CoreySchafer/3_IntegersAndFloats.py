num = 3
print(type(num)) # <class 'int'>
print(type(3.14)) # <class 'float'>

# Arithmetic Operators:
# Addtition: 3+2
# Subtraction: 3-2
# Multiplication: 3*2
# Division: 3/2  = 1.5
# Floor Division: 3//2  = 1 (drops decimals)
# Exponent: 3**2
# Modulus: 3%2  = 1
print(3*(2+1)) # returns 9

# Incrementing values
num = 1
num +=1
print(num)
num*=10
print(num)

# Absolute value functions: removes the sign from -ve numbers
print(abs(-3)) # returns 3

# Round function
print(round(3.5)) # returns 4
print(round(3.75, 1)) # returns 3.8; rounds to the first digit after the decimal

# Comparison Operators
# Equal: 3==2
# Not equal: 3!=2
# Greater than: 3>2
# Less than: 3<2
# Greater or Equal: 3>=2
# Less or Equal: 3<=2
num_1=3
num_2=2
print(num_1==num_2) # returns false
print(num_1>=num_2) # returns true

# CASTING
num_3 = '100'
num_4 = '200'
print(num_3+num_4) # returns 100200
num_3 = int(num_3)
num_4 = int(num_4)
print(num_3+num_4) # returns 300
