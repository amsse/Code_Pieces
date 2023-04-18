# In this challenge, the user enters a string and a substring.
# You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.
#
# Output the integer number indicating the total number of
# occurrences of the substring in the original string.

def count_substring(s, sub):
    return [s[i:i+len(sub)] for i in range(len(s))].count(sub)
    # s[i:i+len(sub)] , ou, "fatia de s desde i para i+len(sub)", É a substring que se está buscando.
    # for i in range(len(s)) , ou, " i in range de número de itens no objeto s", É o campo de busca da substring.
    # .count(sub) É o número de ocorrências da substring (que é retornada).


# outra maneira de solucionar a questão (usando while):
# def count_substring(string, sub_string):
#    count = 0
#    i = string.find(sub_string)
#    while i != -1:
#        count += 1
#        i = string.find(sub_string, i+1)
#    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)