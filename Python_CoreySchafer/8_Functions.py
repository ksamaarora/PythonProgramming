# Function Without Parameters

def hello_func():
    print('Hello')

hello_func() # Hello

def hello_func():
    return 'Hello'

print(hello_func().upper()) # HELLO


# Function wit Parameters

def hello_func1(name,greeting):
    return '{} {} Function'.format(greeting,name)

print(hello_func1('Ksama','Hi')) # Hi Ksama Function


# Args and Kwargs
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='John', age=22)
# ('Math', 'Art')
# {'name': 'John', 'age': 22}


courses = ['Math', 'Art']
info = {'name': 'ksama', 'age':22}
student_info(*courses,**info)
# ('Math', 'Art')
# {'name': 'ksama', 'age': 22}


# EXAMPLE
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2017)) # returns False
print(days_in_month(2017,2)) # returns 28


