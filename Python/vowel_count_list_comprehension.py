def get_count(sentence):
    letter_list = [x for x in sentence] # list comprehension
    vowels_list = ['a','e','i','o','u']
    exist_count = 0
    for x in letter_list:
        if x in vowels_list:
            exist_count = exist_count +1
    return(exist_count)
        

get_count('Hello') #testing




################## REGEX ####################
#
#
#    import re
#    def getCount(str):
#        return len(re.findall('[aeiou]', str, re.IGNORECASE))
#
#
#############################################



################ ONE LINER #################
#
#
#    def getCount(s):
#        return sum(c in 'aeiou' for c in s)
#
#
###########################################