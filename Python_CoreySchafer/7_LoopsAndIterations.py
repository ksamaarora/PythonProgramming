# FOR LOOPS

nums = [1,2,3,4,5]
for num in nums:
    print(num) # returns 1 2 3 4 5

# Break Statement
for num in nums:
    if num==3:
        print('Found!')
        break
    print(num) # returns 1 2

# Continue Statement
for num in nums:
    if num==3:
        continue # Skips 3
    print(num) # returns 1 2 4 5

# Loop in Loop
for num in nums:
    for letter in 'abc':
        print(num,letter) # returns 1 a 1 b 1 c 2 a 2 b 2 c ...

for i in range(1,11):
    print(i) # returns 1 2 3 4 ... 10

# WHILE LOOPS

x = 0
while x<10:
    if x==5:
        break
    print(x) # returns 0 1 2 3 4
    x+=1










