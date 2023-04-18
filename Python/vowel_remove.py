def disemvowel(string):
    for i in "aeiouAEIOU":
        string = string.replace(i, "")
    return string

# test
# disemvowel('This website is for losers LOL!')

