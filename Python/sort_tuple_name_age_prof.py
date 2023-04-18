def short_bio(person):
    name = ''
    age = 0
    profession = ''
    i = 0
    
    for name, age, profession in person:
        name, age, profession = person[i]
        i += 1
    
    return("{} is {} years old and works as a {}".format(name, str(age), profession))
    

print(short_bio([('Mick Jagger', 30, 'Vocalist'), ('Keith Richards', 30, 'Guitarist')]))