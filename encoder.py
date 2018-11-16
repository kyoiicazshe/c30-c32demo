# open unencoded.txt as variable f then close

def randomNumber(seed):
    seed = 3.9 * seed * (1 - seed)
    return (seed)

def convertRandom(number):
    return (int(26 * number))

def encodeLetter(letter, randomOffset, alphaOffset, direction):
    encodedLetter = ord(letter) # (a -> 97)
    encodedLetter -= alphaOffset
    # add 26 so if it's negative it still turns into a number between
    # 0 and 26 (for when we subtract to decode)
    encodedLetter += 26
    # add offset to encodedLetter
    encodedLetter += (randomOffset*direction) # (97+13=110)
    encodedLetter = encodedLetter % 26
    encodedLetter += alphaOffset
    # turn back into a letter
    encodedLetter = chr(encodedLetter) # (110->n)
    return encodedLetter

def encodeString(initialString, seed, direction):
    encodedString = "" #offset = 13	# for rot13
    # loop through letters in initialString
    for letter in initialString:
        if letter.isalpha():  # Only encode letters

            # get random offset
            seed = randomNumber(seed)
            offset = convertRandom(seed)

            encodedLetter = encodeLetter(letter,offset,97, direction)
            encodedString += encodedLetter #(... -> ...n)

        else:  # Keep non-letter characters as they were
            encodedString += letter
    return encodedString

with open('unencoded.txt') as f:
    # read f and store contents in variable read_data
    initialString = f.read()
# print contents of initialString
print(initialString)

# make initialString lowercase
initialString = initialString.lower()

# make empty string
seed = 0.1

encoded = encodeString(initialString, seed, 1)
   
print(encoded)

seed = 0.1
unencoded = encodeString(encoded, seed, -1)

print(unencoded)
