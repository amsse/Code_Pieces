def string_to_array(s):
    if s == "":
        return [""]
    else:
        pass
    
    listed_arr = [i for i in s.split()]
    return(listed_arr)


# testing
# string_to_array("Robin Singh")



########## ONE LINER ###########
#
#    def string_to_array(s):
#        return s.split(" ")
#
################################



########## ONE LINER ###########
#
#    def string_to_array(string=''):
#        return string.split() if string else ['']
#
################################