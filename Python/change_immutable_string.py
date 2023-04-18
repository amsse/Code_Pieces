# You are given an immutable string, and you want to make changes to it.
# How to do it? Slice the string and join it back.

def mutate_string(string, position, character):
    return s[:int(i)]+c+s[int(i)+1:]
    # s[:int(i)] É uma string do início até a posição i (alvo de substituição).
    # +c É o caractere que vamos introduzir (na posição i).
    # +s[int(i)+1:] É a posição na string em que o caractere será substituido.


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)