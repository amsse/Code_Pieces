'''
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
'''

def expanded_form(num):
    exp = [] #expandend form
    zeros = len(str(num))
    for digit in str(num):
        zeros = zeros -1
        if digit != '0':
            exp.append(digit + '0'*zeros)
    print(' + '.join(exp))
    
expanded_form(42)