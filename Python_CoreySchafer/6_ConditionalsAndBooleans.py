language = 'C++'

if language == 'Python':
    print('Language is Python')
elif language == 'C++':
    print('Language is C++')
else:
    print('No match')

# and
# or
# not

user = 'Admin'
logged_in = True

if user == 'Admin' or logged_in == False:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')


a = [1,2,3]
b = [1,2,3]
print(a==b) # True
print(a is b) # False because a and b are two different objects in memory
print(id(a)) # 4378491840
print(id(b)) # 4378811136

c = a
print(id(a)==id(c)) # True

# False Values
  # False
  # None
  # Zero of any numeric type
  # Any empty sequence '', (), []
  # Any empty mapping {}
condition=()
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# returns Evaluated to False

