def digitize(n):
    num_list = [int(i) for i in str(n)]
    num_list.reverse()
    return(num_list)

digitize(35231) #returns [1,3,2,5,3]



############# ONE LINER ###############
#
#    def digitize(n):
#        return map(int, str(n)[::-1])
#
'''
The map function takes two parameters,'function' and 'iterable'.
It applies the funtion on the iterable, in this case formatted as
string and read backwards.

'''
#
#
#######################################