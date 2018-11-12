# open unencoded.txt as variable f then close
with open('unencoded.txt') as f:
    # read f and store contents in variable read_data
    read_data = f.read()
# print contents of read_data
print(read_data)

# make empty string
encodedString = ""

# loop through letters in read_data
for letter in read_data:
    encodedLetter = ord(letter)
    # add 13 to encodedLetter
    encodedLetter += 13
    # turn back into a letter
    encodedLetter = chr(encodedLetter)
    encodedString += encodedLetter
print(encodedString)

uncodedString = ""
 
for letter in encodedString:
    uncodedLetter = ord(letter)
    uncodedLetter -= 13
    uncodedLetter = chr(uncodedLetter)
    uncodedString += uncodedLetter
print(uncodedString)
