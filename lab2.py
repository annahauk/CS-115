'''
Anna Hauk
I pledge my honor that I have abided by the Stevens Honor System
Cs115 Lab 2
'''

def dot(L, K):
    '''output the dot product of the lists L and K'''
    if L == [] and K == []:
        return 0
    return (L[0]*K[0]) + dot(L[1:],K[1:])


def explode(S):
    '''take a string S as input; returns list of the characters in that string'''
    if S == '':
        return []
    return [S[0]] + explode(S[1:])

def ind(e, L):
    '''return the index at which e is first found in L'''
    if L==[]:
        return 0
    elif L[0] == e:
        return 0
    else:
        return ind(e,L[1:]) + 1

def removeAll(e, L):
    '''returns a list that is identical to L with all elements identical to e removed'''
    if L == []:
        return []
    elif e == L[0]:
        return removeAll(e,L[1:])
    else:
        return [L[0]] + removeAll(e,L[1:])

def even(X):
    '''tests if int X is even using modulus'''
    if not X % 2:
        return True
    return False

def myFilter(f, L):
    '''filters list L using condition F'''
    if L == []:
        return []
    elif f(L[0]):
        return [L[0]] + myFilter(f, L[1:])
    else:
        return myFilter(f, L[1:])
    
    
def deepReverse(L):
    '''returns the reversal a list where any element that is a list is also deepReversed'''
    if L == []:
        return []
    if isinstance(L[-1], list):
       return [deepReverse(L[-1])] + deepReverse(L[:-1])
    else:
        return [L[-1]] + deepReverse(L[0:-1])
    










    
