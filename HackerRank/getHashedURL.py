#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getHashedURL' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING url
#  2. STRING hash_string
#  3. INTEGER k
#

def getHashedURL(url, hash_string, k):
    # Write your code here
    import string
    url_blocks = [url[i:i+k] for i in range(0, len(url), k)]
    char_vals = {i: idx for idx, i in enumerate(string.ascii_lowercase)}
    char_vals.update({
        ':': 26,
        '/': 27,
        '.': 28
    })
    hash_value = str()
    for block in url_blocks:
        total = sum([char_vals[i] for i in block])
        hash_val = total % len(hash_string)
        hash_value += hash_string[hash_val]
    
    return hash_value
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    url = input()

    hash_string = input()

    k = int(input().strip())

    result = getHashedURL(url, hash_string, k)

    fptr.write(result + '\n')

    fptr.close()
