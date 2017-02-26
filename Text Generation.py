import string, random

vowels = 'euioay'
consonants = 'qwrtpsdfghjklzxcvbnm'

letters = string.ascii_lowercase

# user input
letter1_input = input("Specify the letter type: Enter 'v' for vowels, 'c' for consonant or 'l' for any letter: ")
letter2_input = input("Specify the letter type: Enter 'v' for vowels, 'c' for consonant or 'l' for any letter: ")
letter3_input = input("Specify the letter type: Enter 'v' for vowels, 'c' for consonant or 'l' for any letter: ")


# string.ascii_lowercase generates all the letters in lowercase
# print(string.ascii_lowercase)

# random.choice() - choose random element from a sequence
# print(random.choice(string.ascii_lowercase))

# generating 3 letter word

def generate3letters():
    if letter1_input =='v':
        letter1 = random.choice(vowels)
    elif letter1_input == 'c':
        letter1 = random.choice(consonants)
    elif letter1_input == 'l':
        letter1 = random.choice(letters)
    else:
        letter1 = letter1_input

    if letter2_input =='v':
        letter2 = random.choice(vowels)
    elif letter2_input == 'c':
        letter2 = random.choice(consonants)
    elif letter2_input == 'l':
        letter2 = random.choice(letters)
    else:
        letter2 = letter2_input

    if letter3_input =='v':
        letter3 = random.choice(vowels)
    elif letter3_input == 'c':
        letter3 = random.choice(consonants)
    elif letter3_input == 'l':
        letter3 = random.choice(letters)
    else:
        letter3 = letter3_input


    threeLetterWord = letter1+letter2+letter3
    return threeLetterWord

# running the function for multiple times
for i in range(20):
    print(generate3letters())