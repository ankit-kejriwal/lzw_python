# Ankit Kejriwal
# akejriw1@uncc.edu
# 801156091

from sys import argv
from struct import pack

dict_size = 256
file_name, bit_length = argv[1:]
MAX_TABLE_SIZE = 2**int(bit_length)
dictionary = {}

# Store the character in the dictionary
for i in range(dict_size):
    dictionary[chr(i)] = i

# Read the content from the input file
input_file_content = open(file_name).read()
output_file = open(file_name.split('.')[0] + ".lzw", 'wb')
print(
    "STRING   SYMBOL  STRING+SYMBOL   STRING+SYMBOL in TABLE?     OUTPUT      TABLEUPDATE"
)
string = ""
symbol = ""
for c in input_file_content:
    symbol = c
    if (string + symbol) in dictionary:
        print(string + "           " + symbol + "         " + string + symbol +
              "               " + "   Y        ")
        string = string + symbol
    else:
        print(string + "          " + symbol + "         " + string + symbol +
              "            " + "     N          " + "            " +
              str(dictionary[string]) + "          " + string + symbol + ":" +
              str(dict_size))
        output_file.write(pack('>H', int(dictionary[string])))
        if dict_size < MAX_TABLE_SIZE:
            dictionary[string + symbol] = dict_size
            dict_size += 1
        string = symbol

# if string is not empty
if string:
    print("" + "          " + '' + "         " + "" + "            " +
          "         Y          " + "            " + str(dictionary[string]))
    output_file.write(pack('>H', int(dictionary[string])))

output_file.close()
