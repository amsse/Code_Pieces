'''
Write a function that takes a string of parentheses, and determines
if the order of the parentheses is valid. The function should return
true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain
any valid ASCII characters. Furthermore, the input string may be empty
and/or not contain any parentheses at all. Do not treat other forms of
brackets as parentheses (e.g. [], {}, <>).
'''

def valid_parentheses(string):
    stack = []
    for i in string:
        if(i == '('):
            stack.append(i)   # adds a parentheses to the list
        elif(i == ')'):
            try:
                stack.pop()   # removes the added parenthesis form the list
            except:           # if there was one added, else it returns False
                return False

    if(len(stack) == 0):      # means that for every valid item added to the list,
        return True           # another valid one was rewmoved (= sum 0)
    else:
        return False