def square_sum(numbers):
    num_sqrd = [x**2 for x in numbers]
    return(sum(num_sqrd))
    
    
square_sum([1,2,2])



############### ONE LINER ################
#
#
#    def square_sum(numbers):
#    return sum(x ** 2 for x in numbers)
#
#
##########################################