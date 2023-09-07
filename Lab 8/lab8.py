'''
Anna Hauk
I pledge my honor that I have abided by the stevens honor system.
CS 115
Lab 8
'''

import sys
import importlib

def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

Factorial = """
# Input: n 
# Assume: n >= 0
# Output: n!
#

# register usage: r1 for the input, r13 for the output

0       read    r1         # Get n
1       setn    r13 1      # initialize r13
2       jeqzn   r1 6       # done if r1 is 0
3       mul     r13 r13 r1 # change r13 = r13 * r1
4       addn    r1 -1      # change r1 = r1 - 1
5       jumpn   2          # repeat
6       write   r13
7       halt
"""

Fibonacci="""
0 read r1  #read n input 
1 jeqzn r1 19 #if n== 0, jump to halt
2 setn r2 0 # trailing num
3 setn r3 1 # leading num
4 write r2 #prints 0 
5 addn r1 -1 #decrements the n
6 jeqzn r1 19 #checks if n==0, if true then halts
7 write r3 #prints out the next number since n!=0 or 1 
8 addn r1 -1 #decrements n again
9 jeqzn r1 19 # checks and halts if n == 0

#calculation

10 add r2 r2 r3 # r2 = r2+r3 trailing = trailing num + leading num
11 write r2 #prints r2
12 addn r1 -1   #decrement counter
13 jeqzn r1 19 #checks if n==0
14 add r3 r3 r2   #r3 = r3 + r2 # leading num = leading num + trailing num
15 write r3 #prints r3
16 addn r1 -1   #decrement counter (n)
17 jeqzn r1 19 # check if counter is 0
18 jumpn 10 #loops back to the calculation if more numbers to process
19 halt #Terminates program
"""


Fibonacci= """


"""



RunThis = Fibonacci

# Choose whether to use debug mode; uncomment one of the following lines.
#Mode = ['-n'] # not debug mode, 
Mode = ['-d'] # debug mode
#Mode = []     # prompt for whether to enter debug mode

if __name__ == "__main__" : 
    import hmmmAssembler ; importlib.reload(hmmmAssembler)
    import hmmmSimulator ; importlib.reload(hmmmSimulator)
    hmmmAssembler.main(RunThis) # assemble input into machine code file out.b
    hmmmSimulator.main(Mode)    # run the machine code in out.b
