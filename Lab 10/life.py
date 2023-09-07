'''
# life.py - Game of Life lab
#
# Anna Hauk
# I pledge my honor that I have abided by the stevens Honor system
# CS 115
# Lab 10
'''
'''
Dies if:
0 or 1 neighbors
4 or more neighbors

revives if:
3 neighbors
'''

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def printBoard( A ):
    """ this function prints the 2d list-of-lists
        A without spaces (using sys.stdout.write)"""
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )


def diagonalize(width,height):
    """ creates an empty board and then modifies it so that it has
    a diagonal strip of "on" cells."""
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(width,height):
    """ creates an empty board and then modifies it so that it has
    an inner square of ones(border of zeros"""
    A = createBoard( width, height )
    for row in range(1,height-1):
        for col in range(1,width-1):
                A[row][col] = 1
    return A

def randomCells(width,height):
    """ returns an array of randomly-assigned 1's and 0's except that
    the outer edge of the array is still completely empty (all 0's)"""
    A = createBoard( width, height )
    for row in range(1,height-1):
        for col in range(1,width-1):
                A[row][col] = random.choice([0,1])
    return A

def copy(A):
    '''makes a deep copy of the input array to the new output arrray '''
    height = len(A)
    width = len(A[0])
    B = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            B[row][col] = A[row][col]

    return B

def innerReverse(A):
    '''takes an old 2d array (or "generation") and then creates a new
    generation of the same shape and size '''
    height = len(A)
    width = len(A[0])
    B = createBoard(width, height)
    for row in range(1, height-1):
        for col in range(1, width-1):
            if A[row][col] == 1:
                B[row][col] = 0
            else:
                B[row][col] = 1
    return B

'''
Dies if:
0 or 1 neighbors
4 or more neighbors

revives if:
3 neighbors
'''
def countNeighbors(row,col,A):
    '''returns an int of alive neighbors'''
    count=0
    if A[row-1][col-1] == 1: #NW
        count+= 1
    if A[row-1][col] == 1: #N
        count+= 1
    if A[row-1][col+1] == 1: #NE
        count+= 1
    if A[row][col-1] == 1:#W
        count+= 1
    if A[row][col+1] == 1: #E
        count+= 1
    if A[row+1][col-1] == 1: #SW
        count+= 1
    if A[row+1][col] == 1: #S
        count+= 1
    if A[row+1][col+1] == 1: #SE
        count+= 1
    return count
    
            
def next_life_generation(A):
    """ makes a copy of A and then advanced one generation of Conway's
    game of life within the *inner cells* of that copy. The outer edge
    always stays 0."""
    width = len(A[0])
    height = len(A)
    B = createBoard(width,height)
    for row in range(1, height-1):
        for col in range(1, width-1):
            count = countNeighbors(row,col,A)
            if count<2 or count>3:
                B[row][col] = 0
            elif count == 3:
                B[row][col] = 1
            else:
                B[row][col] = A[row][col]
    return B
'''

def testCreate():
    A = createBoard(5, 3)
    assert A == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
testCreate()
print("Create Board success!")

def testinner():
    A = innerCells(5,5)
    printBoard(A)
testinner()
print("Inner success!")

def testcopy():
    oldA = createBoard(2,2)
    newA = oldA
    oldA[0][0] = 1
    assert newA[0][0] == 1
testcopy()
print("Copy Success!")

def testrandom():
    A = randomCells(10,10)
    printBoard(A)
testrandom()
print("Random Success!")

def testreverse():
    A = randomCells(8,8)
    A2 = innerReverse(A)
    printBoard(A2)
testreverse()
print("Reverse Success!")

def testNextLife():
    A = [ [0,0,0,0,0], 
      [0,0,1,0,0], 
      [0,0,1,0,0], 
      [0,0,1,0,0], 
      [0,0,0,0,0]]
    printBoard(A)
    A2 = next_life_generation( A )
    print("#########")
    printBoard(A2)
testNextLife()
print("Next Life success!")
'''
