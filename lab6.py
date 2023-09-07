'''
Anna Hauk
I pldege my honor that I have abided by the Stevens Honor System.
CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 != 0
'''
#42 in Base 2 = 101010

2. For an odd number in base 2, the rightmost bit will be 1 because all of
the other bits are compromised of even numbers so you need the one to make it odd
but even would be 0 for similar reasons
3. Slicing the rightmost bit off is doing integer divison by 2
4. Y would help us find N by adding a 1 to the end if the number is odd and 0 if
it is even 
'''

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    bit = '1' if isOdd(n) else '0'
    return numToBinary(n//2) + bit

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=='':
        return 0
    if s[-1]=='1':
        return 1 + 2 * binaryToNum(s[:-1])
    else:
        return 2 * binaryToNum(s[:-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    num =  binaryToNum(s)
    if num==255:
        num=0
    else:
        num=num+1
    binary_result = numToBinary(num)
    return  "0" * (8-len(binary_result)) + binary_result

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if (n==0):
        print(s)
    else:
        print(s)
        y=increment(s)
        count(y,n-1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    
    if n == 0:
        return ''
    if n % 3 == 0:
        bit='0'
    if n % 3 == 1:
        bit='1'
    if n % 3 == 2:
      bit = '2'
    return numToTernary(n//3) + bit
'''
59 in ternary is 2012. Doing the modulus way, the remainders become 2,1,0,2 and
thats the ternary representation
'''

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s=='':
        return 0
    if s[-1]=='1':
        return 1 + 3 * ternaryToNum(s[:-1])
    if s[-1]=='2':
        return 2 + 3 * ternaryToNum(s[:-1])
    if s[-1]=='0':
        return 0 + 3 * ternaryToNum(s[:-1])



