# open unencoded.txt as variable f then close

def myRandom(seed):
    seed = 3.9 * seed * (1 - seed)
    return (seed)

def convertRandom(number):
    return (int(256 * number))

with open('unencoded.txt') as f:
    # read f and store contents in variable read_data
    read_data = f.read()
# print contents of read_data
print(read_data)

# make empty string
encodedString = ""
# set seed for random number sequence
'''originalSeed = 0.25
seed = originalSeed'''
offset = 13	# for rot13

# loop through letters in read_data
for letter in read_data:
    print(letter + " " + str(letter.isalpha()))
    encodedLetter = ord(letter)
    '''seed = myRandom(seed)
    offset = convertRandom(seed)'''
    # add offset to encodedLetter
    encodedLetter += offset
    # turn back into a letter
    encodedLetter = chr(encodedLetter)
    encodedString += encodedLetter
print(encodedString)

'''uncodedString = ""

#seed = originalSeed 
for letter in encodedString:

    #seed = myRandom(seed)
    #offset = convertRandom(seed)
    uncodedLetter = ord(letter)
    uncodedLetter -= offset
    uncodedLetter = chr(uncodedLetter)
    uncodedString += uncodedLetter
print(uncodedString)'''
