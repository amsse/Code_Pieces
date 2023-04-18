# Python program to find the element occurring odd number of times

def find_it(seq):
 
    # variable for result
    res = 0
     
    # Traverse the array
    for element in seq:
        # Logical XOR (only true when number of true operators is odd)
        res = res ^ element
 
    return res
 
# Test array
seq = [1,1,2]
 
print("%d" % find_it(seq))



############# FASTER ################
#
#
#    def find_it(seq):
#        for i in seq:
#            if seq.count(i)%2!=0:
#                return i
#
#
#####################################




############# LOGICAL ################
#
#    import operator
#
#    def find_it(xs):
#        return reduce(operator.xor, xs)
#    
######################################