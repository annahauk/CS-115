'''
Anna Hauk
I pledge my honor that I have abided by the Stevens Honor System
Cs115 Lab 3
'''

def change(amount, coins):
    '''return a non-negative integer indicating the minimum number of coins required to make up the given amount'''
    if coins != []:
        if coins[0] < 0:
            print('Negative coin value passed in')
            return float('inf')
    if coins == [] or amount < 0:
        return float('inf') 
    if amount == 0:
        return 0
    else:
        useIt = change(amount-coins[0],coins) + 1 #not slicing coins; can use as many coins at index
        loseIt = change(amount, coins[1:])
    return min(useIt, loseIt)


