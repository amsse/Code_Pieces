# Game Rules:
# Both players are given the same string, s.
# Both players have to make substrings using the letters of the string s.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring:
# A player gets +1 point for each occurrence of the substring in the string s.

def minion_game(string):
    vowels = 'AEIOU'  # lista de vogais.

    kevsc = 0  # kevin score
    stusc = 0  # stuart score
    for i in range(len(s)):  # range determinado pelo length da palavra no string.
        if s[i] in vowels:  # se o "i" estiver na lista de vogais.
            kevsc += (len(s)-i)  # pontuação será o tamanho da palavra menos a letra usada.
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)