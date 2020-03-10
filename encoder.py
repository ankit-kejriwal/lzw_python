# Ankit Kejriwal
# akejriw1@uncc.edu
# 801156091

from sys import argv
from struct import pack

dictionary_size = 256
file_name, bit_length = argv[1:]
MAX_TABLE_SIZE = 2**int(bit_length)
encoder_dictionary = {}

# Store the character in the dictionary
for i in range(dictionary_size):
    encoder_dictionary[chr(i)] = i

# Read the content from the input file
input_file_content = open(file_name).read()
output_file = open(file_name.split('.')[0] + ".lzw", 'wb')
print(
    "STRING   SYMBOL  STRING+SYMBOL   STRING+SYMBOL in TABLE?     OUTPUT      TABLEUPDATE"
)
string = ""
sym = ""
for c in input_file_content:
    sym = c
    if (string + sym) in encoder_dictionary:
        print(string + "           " + sym + "         " + string + sym +
              "               " + "   Y        ")
        string = string + sym
    else:
        print(string + "          " + sym + "         " + string + sym +
              "            " + "     N          " + "            " +
              str(encoder_dictionary[string]) + "          " + string + sym +
              ":" + str(dictionary_size))
        output_file.write(pack('>H', int(encoder_dictionary[string])))
        if dictionary_size < MAX_TABLE_SIZE:
            encoder_dictionary[string + sym] = dictionary_size
            dictionary_size = dictionary_size + 1
        string = sym

# if string is not empty
if string:
    print("" + "          " + '' + "         " + "" + "            " +
          "         Y          " + "            " +
          str(encoder_dictionary[string]))
    output_file.write(pack('>H', int(encoder_dictionary[string])))

output_file.close()
