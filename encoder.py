# open unencoded.txt as variable f then close
with open('unencoded.txt') as f:
    # read f and store contents in variable read_data
    read_data = f.read()
# print contents of read_data
print(read_data)

# loop through letters in read_data
for letter in read_data:
    # print the next letter
    print(letter)

