'''
Anna Hauk
I pledge my honor that I have abided by the Stevens Honor System
Cs 115 HW3
'''

def addOne(l):
    '''adds 1 to every element of list'''
    if l == []:
        return []
    return [l[0]+1] + addOne(l[1:])

def explode(s):
    '''takes string elements and returns a list of each character'''
    if s == '':
        return []
    return [s[0]] + explode(s[1:])

def even(n):
    '''checks if number is evenly divisible by 2'''
    return n%2==0

def myFilter(func,l):
    '''replicates the filter function; returns list of true elements from passed in function'''
    if l == []:
        return []
    elif func(l[0]) == True:
        return [l[0]] + myFilter(func,l[1:])
    else:
        return myFilter(func,l[1:])
    
def sumPos(l):
    '''returns a sum of the positive integers in list'''
    if l ==[]:
        return 0
    elif l[0] <= 0:
        return 0 + sumPos(l[1:])
    else:
        return l[0] + sumPos(l[1:])
