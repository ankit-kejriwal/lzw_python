**@name Ankit Kejriwal<br />
@studentID 801156091**

# Project 1: LZW Compression<br />

## **Introduction:**<br />

The Lempel–Ziv–Welch (LZW) algorithm is a lossless documents compression algorithm. LZW is an adaptive compression set of regulations that does now not anticipate prior information of the enter data distribution. This set of guidelines works well when the input records is sufficiently large and there's redundancy inside the statistics.Two examples of commonly used report codecs that use LZW compression are the GIF photograph layout served from internet websites and the TIFF photo format. LZW compression is also terrific for compressing textual content files, and is the algorithm inside the compress Unix record compression utility.

## **Application of LZW:**<br />

GIF files<br />
TIFF files<br />
PDF files<br />
Unix Compress, gzip<br />

## **Steps in LZW Algorithm**<br />

Encoder<br />
Decoder<br />
Input File --> Encoded File --> Decoded File<br />
In the first step encoding is done by encoding.py<br />
In the second step decoding is done by decoding.py<br />

## **Pseudocode of Encoding**<br />

MAX_TABLE_SIZE=2(bit_length) //bit_length is number of encoding bits<br />
initialize TABLE[0 to 255] = code for individual characters <br />
STRING = null <br />
while there are still input symbols: <br />
SYMBOL = get input symbol <br />
if STRING + SYMBOL is in TABLE: <br />
STRING = STRING + SYMBOL <br />
else: <br />
output the code for STRING <br />
If TABLE.size < MAX_TABLE_SIZE: <br />
add STRING + SYMBOL to TABLE // STRING + SYMBOL now has a code <br />
STRING = SYMBOL <br />
output the code for STRING <br />

## **Pseudocode of Decoding**<br />

MAX_TABLE_SIZE=2(bit_length) <br />
initialize TABLE[0 to 255] = code for individual characters <br />
CODE = read next code from encoder <br />
STRING = TABLE[CODE] <br />
output STRING <br />
while there are still codes to receive: <br />
CODE = read next code from encoder <br />
if TABLE[CODE] is not defined: <br />
NEW_STRING = STRING + STRING[0] <br />
else: <br />
NEW_STRING = TABLE[CODE] <br />
output NEW_STRING <br />
if TABLE.size < MAX_TABLE_SIZE: <br />
add STRING + NEW_STRING[0] to TABLE <br />
STRING = NEW_STRING <br />

## **Program Description**<br />

Programming Language : Python 3.7.3 <br />

To Run the encoder.py, two arguments are required<br />
filename - The file to be compresssed <br />
Bitlength - to get the max length of table <br />
Command to run program <br />
python3 encoder.py input1.txt 9 <br />

To Run the decoder.py, two arguments are required <br />
filename - The file to be decompressed <br />
Bitlength - to get the max length of table<br />
Command to run program <br />
python3 decoder.py input1.lzw 9 <br />

## **Data Structure**<br />

Dictionary is used to put into effect the algorithm. It containes the ASCII characters as KEY alongside with its ascii price as VALUE for encoding and vice versa in case of decoding.

Note <br />
open function is used for reading and writing to files. <br />
For encoding, encoder.py file is used. It will generate compressed file. <br />
For decoding, decoder.py is used. It will generate decoded textual content file, whose contents will be equal as the preliminary enter file. <br />

## **References:**<br />

https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch <br />
https://www.youtube.com/watch?v=j2HSd3HCpDs <br />
