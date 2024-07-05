print("Hello world")

message = 'Hello world'
print(message)

message1 = 'Bobby\'s world'
print(message1)

message2 = """ hey whats up
helloo
heyuu"""
print(message2)

# Length Function
print(len(message)) # prints 11

# Slicing
print(message[4]) # prints o
print(message[0:5]) # prints Hello; index 0 incl but index 5 excl
print(message[6:]) # prints world index 6 to end

# Lower & Upper method
print(message.lower()) # hello world
print(message.upper()) # HELLO WORLD

# Count method
print(message.count('Hello')) # prints 1
print(message.count('l')) # prints 3

# Find method
print(message.find('world')) # prints 6 because world starts at index 6
print(message.find('universe')) # prints -1 because word cannot be found

# Replace method
message3 = message.replace('world', 'universe') # .replace('oldword', 'newword')
print(message3) # Hello universe

# Concatenate string

# Using + sign
greeting = "Hello"
name = "Ksama"
message4 = greeting + ', ' + name + '. Welcome!'
print(message4) # Hello, Ksama. Welcome!

# Using PlaceHolders
message5 = '{}, {}. Welcome!'.format(greeting, name)
print(message5) # Hello, Ksama. Welcome!

# Using f strings - write code within placeholder
message6 = f'{greeting}, {name.upper()}. Welcome!'
print(message6) # Hello, KSAMA. Welcome!

print(dir(name))

