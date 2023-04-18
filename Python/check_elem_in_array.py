'''
You will be given an array 'a' and a value 'x'. All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not.
'''


def check(seq, elem):
    if seq.count(elem):
        return True
    else:
        return False
    
    
########### MY FIRST ONE LINER #############
#
#
#   def check(seq, elem):
#       return True if seq.count(elem) else False
#
#
############################################



########### BETTER ONE LINER ###############
#
#
#    def check(seq, elem):
#        return elem in seq
#
#
############################################