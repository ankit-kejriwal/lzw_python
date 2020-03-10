# Ankit Kejriwal
# akejriw1@uncc.edu
# 801156091

from sys import argv
from struct import unpack

dict_size = 256
file_name, bit_length = argv[1:]
MAX_TABLE_SIZE = 2**int(bit_length)
dictionary = {}

# Store the character in the dictionary
for i in range(dict_size):
    dictionary[i] = chr(i)

# Read the content from the input file
input_file_content = open(file_name, "rb")
output_file = open(file_name.split('.')[0] + "_decoded.txt", 'w')

# Read the first 16 bit value , decode and write the character to the output_file
data = input_file_content.read(2)
(code, ) = unpack('>H', data)
string = dictionary[code]
output_file.write(string)

data = input_file_content.read(2)
while (len(data) == 2):
    (code, ) = unpack('>H', data)
    if code not in dictionary:
        new_string = string + string[0]
    else:
        new_string = dictionary[code]
    if len(dictionary) < MAX_TABLE_SIZE:  # check if table is not full
        dictionary[dict_size] = string + new_string[0]
        dict_size += 1
    output_file.write(new_string)  # write the new string to the output file
    string = new_string
    data = input_file_content.read(2)
output_file.close()
input_file_content.close()