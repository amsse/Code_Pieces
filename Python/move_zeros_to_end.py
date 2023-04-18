'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''

def move_zeros(lst):
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
    return lst



############## ONE LINER ###############
#
#
#    def move_zeros(array):
#        return [ i for i in array if i != 0]+[ i for i in array if i == 0]
#
#
########################################