'''
Anna Hauk
I pledge my honor that I have abided by the Stevens Honor System.
Nov 6
CS115 - Hw 5
'''

# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.


def binary(base10, num = 0):
    """converts base 10 to base 2 and outputs it in 5 bit blocks"""
    #base10 is number we're converting
    #num is the number of bits we have after binary conversion
    if base10 == 0:
        return "0" * (COMPRESSED_BLOCK_SIZE - num)
    toAdd = "0" if base10 % 2 == 0  else "1"
    return binary(base10//2, num + 1) + toAdd

def compress(s, updatedLength = 0, bit_looking_for = "0"):
    """takes a binary string s of length 64 as input and returns another binary string as output"""
#s = string to compress
#updatedLength = counts how many #s in row
#count = tracks digit we're counting
#returns compressed string

    if s == "":
        if updatedLength != 0: #if s is empty, return what we have
            a = binary(updatedLength)
            return a
        else:
            return ""

#if you can't run it anymore, just return what you have and start again  
    if updatedLength == MAX_RUN_LENGTH or bit_looking_for != s[0]:
        a = binary(updatedLength)
        return a + compress(s, 0,"0" if bit_looking_for == "1" else "1")
    
# if updatedLength < 0 && next string matches bit_looking_for
    return compress(s[1:], updatedLength + 1, bit_looking_for)



### Answer to compress question
"""the pathologic case would be for alternating
       zeros and ones, but starting with a 1 in which
       case our compression algorithm would output
       65*COMPRESSED_BLOCK_SIZE bit strings for a total of 325 bits
       in our case of COMPRESSED_BLOCK_SIZE being 5
       largest num of bits = 325
"""

def binaryToNum(s):
    """returns the int corresponding to binary representation"""
    if s == "":
        return 0
    b = 2 ** (len(s) - 1)
    return int(s[0]) * b + binaryToNum(s[1:])

def uncompress(s, c = "0"):
    """passed in compress(s) and undoes the compress func"""
    if s == "":
        return ""

    numWork = int(binaryToNum(s[0:COMPRESSED_BLOCK_SIZE]))
    return (c * numWork) + uncompress(s[COMPRESSED_BLOCK_SIZE:], "1" if c == "0" else "0")


def compression(s):
    """returns ration of compressed size compared to origional size of image s"""
    return len(compress(s)) / len(s)


#Answer to Compression question


def print_image(s):
    for i in range(len(s)//8): 
        raster_line=''
        for j in range(8):
            if s[i*8+j]=='1':
                raster_line=raster_line+'X'
            else:
                raster_line=raster_line+' '
        print(raster_line)
                
# penguin
print_image("00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100")
print("-"*10)
# smile
print_image("0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8)
print("-"*10)
# five
print_image("1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0")



"""
Professor Lai is wrong because

A 64 bit string is a data type. If the 64 bit string it empty, there is no compression algorithm
that is less than a length of 0. you can return "" for an empty 64-bit string but len("") is not
< len(the empty 64 bit string) as 0 == 0
"""

