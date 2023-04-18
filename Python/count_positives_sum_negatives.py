def count_positives_sum_negatives(arr):
    positives_list = []
    negatives_list = []
    for x in arr:
        if x > 0:
            positives_list.append(x)
        elif x < 0:
            negatives_list.append(x)
    
    #positives
    count_of_positives = (len(positives_list))
    
    #negatives
    sum_of_neg = []
    sum_of_neg.append(sum(negatives_list))
    
    #return format
    answer_list = []
    answer_list.append(count_of_positives)
    answer_list.append(sum_of_neg[0])
    
    if len(arr) !=0:
        return answer_list
    else:
        return []
        # use print to check

count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
# should return [10, -65]


############ ONE LINER #############
#
#
#    return [len([i for i in arr if i > 0]), sum([i for i in arr if i < 0])] if len(arr) != 0 else []
#
#
####################################