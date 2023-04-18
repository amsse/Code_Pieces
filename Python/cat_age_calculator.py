'''
Cat Age Calculator

The first year of a cat equivalates to 15 human years;
The second year equivalates to another 9 more years;
The next years equivalate to 4 years each.

'''

def catAge(n):
    age = 0
    if n <= 0:
        age = "Baby cat"
    # year one:
    elif n == 1:
        age = 15
    # year two:
    elif n == 2:
        age = (15+9)
    # next years:
    else:
        age = (24 + ((n-2)*4))
        
    return age

#testing
print(catAge(0))
    