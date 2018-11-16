# open unencoded.txt as variable f then close

def randomNumber(seed):
    seed = 3.9 * seed * (1 - seed)
    return (seed)

def convertRandom(number):
    return (int(26 * number))

with open('unencoded.txt') as f:
    # read f and store contents in variable read_data
    initialString = f.read()
# print contents of initialString
print(initialString)

# make initialString lowercase
#initialString = initialString.lower()
#print(initialString)

# make empty string
encodedString = "" #offset = 13	# for rot13
seed = 0.1

# loop through letters in initialString
for letter in initialString:
    if letter.isalpha():  # Only encode letters
        encodedLetter = ord(letter) # (a -> 97)
        seed = randomNumber(seed)
        offset = convertRandom(seed)
        #encodedLetter = encodedLetter - 97
        encodedLetter -= 97
        # add offset to encodedLetter
        encodedLetter += offset # (97+13=110)
        encodedLetter = encodedLetter % 26
        encodedLetter += 97
        # turn back into a letter
        encodedLetter = chr(encodedLetter) # (110 -> n)
        encodedString += encodedLetter #(... -> ...n)
    else:  # Keep non-letter characters as they were
        encodedString += letter
   
print(encodedString)

uncodedString = ""

#seed = originalSeed 
'''for letter in encodedString:
    if letter.isalpha():
        uncodedLetter = ord(letter)
        uncodedLetter -= offset
        uncodedLetter = chr(uncodedLetter)
    uncodedString += uncodedLetter
print(uncodedString)'''
