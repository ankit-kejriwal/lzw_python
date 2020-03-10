def compress(uncompressed):
    """Compress a string to a list of output symbols."""

    # Build the dictionary.
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    # in Python 3: dictionary = {chr(i): i for i in range(dict_size)}
    ouputfile = open('input.lzw', 'w')
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            ouputfile.write(str(dictionary[w]) + ',')
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary[w])
        ouputfile.write(str(dictionary[w]))
    ouputfile.close()
    return result


def decompress(compressed):
    """Decompress a list of output ks to a string."""
    from io import StringIO

    # Build the dictionary.
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))
    # in Python 3: dictionary = {i: chr(i) for i in range(dict_size)}

    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = StringIO()
    for i in range(0, len(compressed)):
        compressed[i] = int(compressed[i])
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)

        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    ouputfile = open('input_decoded.txt', 'w')
    ouputfile.write(str(result.getvalue()))
    ouputfile.close()
    return result.getvalue()


# How to use:
contents = open('input.txt').read()
compressed = compress(contents)
print(compressed)
decompress_input = open('input.lzw').read()
decompress_input = decompress_input.split(',')
print(decompress_input)
decompressed = decompress(decompress_input)
print(decompressed)
