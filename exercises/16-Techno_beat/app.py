import re

def lyrics_generator(listOfNumbers):
    lyrics = ''
    for numbers in listOfNumbers:
        if numbers == 0:
            lyrics = lyrics + 'Boom '
        if numbers == 1:
            lyrics = lyrics + 'Drop the base '
    
    Regex = re.compile(r'Drop the base Drop the base Drop the base ')
    ModifiesStringOnlyIfMatches = Regex.sub('Drop the base Drop the base Drop the base !!!Break the base!!! ',lyrics)
    return ModifiesStringOnlyIfMatches



# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))

# Regex = re.compile(r'Drop the base Drop the base Drop the base ')
# mo = Regex.sub('Drop the base Drop the base Drop the base !!!Break the base!!!',lyrics_generator([1,0,1]))

# print(mo)

