alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(letter):

# Make all letters lowercase to make function case-insensitive
    letter = letter.lower()
# Iterate through alphabet to locate index of letter 0-25
    if letter in(alphabet):
        alphChar = alphabet.index(letter)

    return alphChar

# Function to rotate character for encryption
def rotate_character(char, rot):
    # if statement to maintain uppercase letters during encryption
    if char.isupper():
        let = (alphabet_position(char))
        newix = (let + rot) % 26
        subLet = alphabet[newix]
        newLet = subLet.upper()
    # elif statement to maintain lowercase letters during encryption
    elif char.islower():
        let = (alphabet_position(char))
        newix = (let + rot) % 26
        newLet = alphabet[newix]
    # else statement to return all non-alphabetic char unchanged
    else:
        newLet = char
    return newLet

def encrypt(message, num_rotations):
    # New sentence string accumulator
    newSentence = ""
    # Function to loop through message and encrypt each letter
    for let in message:
        newLet = rotate_character(let, num_rotations)
        newSentence = newSentence + newLet
    return newSentence