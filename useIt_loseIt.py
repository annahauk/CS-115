'''
Anna Hauk
I pledge my honor that I have abided by the Stevens Honor System
Cs 115 Lab Practice
'''

#cap - int
#items - list
def subset(cap,items):
    '''returns an int with the number of items in bag'''
    if items == [] or cap <0:
        return float('inf')
    if cap == 0:
        return 0
    else:
        useIt= subset(cap-items[0], items[1:]) + 1
        loseIt = subset(cap, items[1:])
    return max(useIt,loseIt)


def subsetClass(cap,items):
    '''returns an int with the number of items in bag'''
    if (items == [] or cap <=0):
        return 0
    first = items[0]
    rest = items[1:]
    if(first> cap):
        return subset(cap, rest)
    elif (first == cap):
        return cap #you could return first
    if (first < cap):
        use_it = subset(cap - first, rest)+ first
        lose_it = subset(cap, rest)
    return max(use_it, lose_it)
