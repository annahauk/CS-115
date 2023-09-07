'''
Anna Hauk
I pledge my honor that I have abided by the Stevens Honor System
CS 115
Lab 9
'''


# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:

def mult(c,n):
    result = 0
    for x in range(n):
        result += c  #c * n
    return result

def test_mult():
    assert mult(6,7) == 42 
    assert mult(1.5,28) == 42.0
print ("Mult success!")
test_mult()

    
def update( c, n ): 
    """ update starts with z=0 and runs z = z**2 + c for
    a total of n times. It returns the final z."""
    result = 0 #z value
    for x in range(n):
        result = result**2 + c
    return result

def test_up():
    assert update(1, 3) == 5
    assert update( -1, 3 ) == -1
    assert update( -1, 10 ) == 0
print ("Update success!")
test_up()


def inMSet(c, n): 
    """ inMSet takes in c for the update step of z = z**2+c n,
    the maximum number of times to run that step Then, it should
    return False as soon as abs(z) gets larger than 2 
            True if abs(z) never gets larger than 2 (for n iterations) 
    """ 

    result = 0 #z value
    for x in range(n):
        result = result**2 + c
        if abs(result) > 2:
            return False
    return True

def test_inMSet():
    assert inMSet(0 + 0j, 25) == True
    assert inMSet(3 + 4j, 25) == False
    assert inMSet(0.3 + -0.5j, 25) == True
    assert inMSet(-0.7 + 0.3j, 25) == False
    assert inMSet(0.42 + 0.2j, 25) == True
    assert inMSet(0.42 + 0.2j, 50) == False
print("inMSet success!")
test_inMSet()

def weWantThisPixel( col, row ): 
    """ a function that returns True if we want the pixel at
    col, row and False otherwise""" 
    if col%10 == 0  and  row%10 == 0: 
        return True 
    else: 
        return False 
 
def test(): 
    """ a function to demonstrate how to create and save a
    png image """
    width = 300 
    height = 200 
    image = PNGImage(width, height) 
 
    # create a loop in order to draw some pixels 
     
    for col in range(width): 
        for row in range(height): 
            if weWantThisPixel( col, row ) == True: 
                image.plotPoint(col, row) 
    # we looped through every image pixel; we now write the file 
    image.saveFile()


def scale(pix, pixMax, floatMin, floatMax): 
    """ scale takes in pix, the CURRENT pixel column (or row)
    pixMax, the total # of pixel columns floatMin, the min
    floating-point value floatMax, the max floating-point value 
    scale returns the floating-point value that corresponds to
    pix"""
    avg = 1.0 * pix/pixMax
    range1 = floatMax - floatMin
    return floatMin + (range1 * avg)

def test_scale():
    assert scale(100, 200, -2.0, 1.0) == -0.5
    assert scale(100, 200, -1.5, 1.5) == 0.0
    assert scale(100, 300, -2.0, 1.0) == -1.0 
    assert scale(25, 300, -2.0, 1.0) == -1.75 
print ("Scale success!")
test_scale()


def mset(): 
    """ creates a 300x200 image of the Mandelbrot set """ 
    width = 300 
    height = 200 
    image = PNGImage(width, height) 
 
    #create a loop in order to draw some pixels 
     
    for col in range(width): 
        for row in range(height): 
            # here is where you will need 
            # to create the complex number, c!
            x = scale(col, width, -2.0, 1.0)
            y = scale(row, height, -1.0, 1.0)
            c = x + y*1j
            if inMSet(c,25) == True: 
                image.plotPoint(col, row) 
 
    # we looped through every image pixel; we now write the file 
 
    image.saveFile()

def mset2(n): 
    """ creates a 300x200 image of the Mandelbrot set """ 
    width = 300 
    height = 200 
    image = PNGImage(width, height) 
 
    #create a loop in order to draw some pixels 
     
    for col in range(width): 
        for row in range(height): 
            # here is where you will need 
            # to create the complex number, c!
            x = scale(col, width, -2.0, 1.0)
            y = scale(row, height, -1.0, 1.0)
            c = (x + y*1j)**n
            if inMSet(c,25) == True: 
                image.plotPoint(col, row) 
 
    # we looped through every image pixel; we now write the file 
 
    image.saveFile() 

    
'''
EXTRA CREDIT
explain how changing n, floatmin, and floatmax change the image

if asking what changing n does (mset()):
as n increases the edges become more distinct and the image looks clearer

if asking find something with n that makes it change (mset2(n)):
Raising the complex number to the nth power, changes the ratio of the resulting number
number. This makes the image repeat patterns in a circular direction and makes it sharper

Increasing floatMin scales the image and decreasing
floatMin truncates the image. Increasing floatMax compressed the image
horizontally while decreasing floatMax expands the image


'''
