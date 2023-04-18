def abbrev_name(name):
    #The str.split() method splits the string into a list of substrings
    fullname = [i[0] for i in name.split()]
    return(("{}.{}".format(fullname[0], fullname[1])).upper())
        # use print for testing!

abbrev_name("Aldous Snow")



#######################
#
#    def abbrevName(name):
#        first, last = name.upper().split(' ')
#        return first[0] + '.' + last[0]
#
#######################