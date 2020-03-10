**@name Ankit Kejriwal<br />
@studentID 801156091**

# Project 1: LZW Compression<br />
## **Introduction:**<br />
The Lempel–Ziv–Welch (LZW) algorithm is a lossless data compression algorithm. LZW is an adaptive compression algorithm that does not assume prior knowledge of the input data distribution. This algorithm works well when the input data is sufficiently large and there is redundancy in the data.Two examples of commonly used file formats that use LZW compression are the GIF image format served from websites and the TIFF image format. LZW compression is also suitable for compressing text files, and is the algorithm in the compress Unix file compression utility.

## **Application of LZW:**<br />
GIF and TIFF files<br />
PDF files<br />
Unix Compress, gzip<br />

## **Two steps of LZW Algorithm**<br />
Encoding/Compressing<br />
Decoding/Decompressing<br />
LZW Algorithm<br />
Input File --> Compressed File --> Decompressed File<br />
First arrow shows the encoding done by encoding.py<br />
Second arrow shows the compressed file is decoded to original text using decoding.py<br />

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

To Run the encoder.py <br />
Two arguments are required <br />
InputfileName - The file to be compresssed <br />
Bitlength - The length to be used <br />
Command to run program <br />
python3 encoder.py input1.txt 9 <br />

To Run the decoder.py <br />
Two arguments are required <br />
InputfileName - The file to be compresssed <br />
Bitlength - The length to be used <br />
Command to run program <br />
python3 decoder.py input1.lzw 9 <br />

## **Data Structure**<br />
Dictionary is used to implement the algorithm. It containes the ASCII characters as KEY along with its ascii value as VALUE for encoding and vice versa in case of decoding.

## **encoder.py**<br />
The enoder uses dictionary and follows Pseudocode of Encoding to encode the input file. Here, In dictionary ASCII Character is the KEY and ASCII Value is the VALUE.
## **decoder.py**<br />
The decoder uses dictionary in opposite fashion, where ASCII Value is the KEY and ASCII Character is the VALUE. It follows the Pseudocode of Decoding to decode the encoded text.

Note <br />
open function is used for reading and writing to files. <br />
For encoding, encoder.py file is used. It will generate compressed (lzw) file. <br />
For decoding, decoder.py is used. It will generate decoded text file, whose contents will be same as the initial input file. <br />
The compression file is created using charset UTF_16BE and stored in 16-bit format.<br />

## **References:**<br />
https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch <br />
https://www.youtube.com/watch?v=j2HSd3HCpDs <br />
