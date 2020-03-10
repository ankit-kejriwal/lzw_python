/**_
@name Ankit Kejriwal
@studentID 801156091
_**/

Project 1: LZW Compression
Introduction:
The Lempel–Ziv–Welch (LZW) algorithm is a lossless data compression algorithm. LZW is an adaptive compression algorithm that does not assume prior knowledge of the input data distribution. This algorithm works well when the input data is sufficiently large and there is redundancy in the data.Two examples of commonly used file formats that use LZW compression are the GIF image format served from websites and the TIFF image format. LZW compression is also suitable for compressing text files, and is the algorithm in the compress Unix file compression utility.

Application of LZW
GIF and TIFF files
PDF files
Unix Compress, gzip

Two steps of LZW Algorithm
Encoding/Compressing
Decoding/Decompressing
LZW Algorithm
Input File --> Compressed File --> Decompressed File
First arrow shows the encoding done by encoding.py
Second arrow shows the compressed file is decoded to original text using decoding.py

Pseudocode of Encoding
MAX_TABLE_SIZE=2(bit_length) //bit_length is number of encoding bits
initialize TABLE[0 to 255] = code for individual characters
STRING = null
while there are still input symbols:
SYMBOL = get input symbol
if STRING + SYMBOL is in TABLE:
STRING = STRING + SYMBOL
else:
output the code for STRING
If TABLE.size < MAX_TABLE_SIZE:
add STRING + SYMBOL to TABLE // STRING + SYMBOL now has a code
STRING = SYMBOL
output the code for STRING

Pseudocode of Decoding
MAX_TABLE_SIZE=2(bit_length)
initialize TABLE[0 to 255] = code for individual characters
CODE = read next code from encoder
STRING = TABLE[CODE]
output STRING
while there are still codes to receive:
CODE = read next code from encoder
if TABLE[CODE] is not defined:
NEW_STRING = STRING + STRING[0]
else:
NEW_STRING = TABLE[CODE]
output NEW_STRING
if TABLE.size < MAX_TABLE_SIZE:
add STRING + NEW_STRING[0] to TABLE
STRING = NEW_STRING

Program Description
Programming Language : Python 3.7.3

To Run the encoder.py
Two arguments are required
InputfileName - The file to be compresssed
Bitlength - The length to be used
Command to run program
python3 encoder.py input1.txt 9

To Run the decoder.py
Two arguments are required
InputfileName - The file to be compresssed
Bitlength - The length to be used
Command to run program
python3 decoder.py input1.lzw 9

Data Structure
Dictionary is used to implement the algorithm. It containes the ASCII characters as KEY along with its ascii value as VALUE for encoding and vice versa in case of decoding.

encoder.py
The enoder uses dictionary and follows Pseudocode of Encoding to encode the input file. Here, In dictionary ASCII Character is the KEY and ASCII Value is the VALUE.
decoder.py
The decoder uses dictionary in opposite fashion, where ASCII Value is the KEY and ASCII Character is the VALUE. It follows the Pseudocode of Decoding to decode the encoded text.

Note
open function is used for reading and writing to files.
For encoding, encoder.py file is used. It will generate compressed (lzw) file.
For decoding, decoder.py is used. It will generate decoded text file, whose contents will be same as the initial input file.
The compression file is created using charset UTF_16BE and stored in 16-bit format.

References:
https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch
https://www.youtube.com/watch?v=j2HSd3HCpDs
