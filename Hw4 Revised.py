##from cs115 import *

memo_change = {}
'''
def fast_change(amount, coins):
    Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.
    coins = tuple(coins)

    if (amount,coins) in memo_change:
        return memo_change[(amount, coins)]
    if amount==0:
       answer = 0
    elif coins == () or amount < 0:
        answer = float("inf")
    else:
        answer = min(1 + fast_change(amount - coins[0], coins), fast_change(amount, coins[1:]))
        memo_change[(amount, coins)] = answer
        return answer



memo_change = {0:0}    
def fast_change(amount, coins):
    Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.
    
    if amount in memo_change:
        return memo_change[amount]
    if amount == 0 and coins == []:
        memo_change[(0,[])] = 0
        return 0
    elif (amount > 0 and coins ==[]) or amount < 0:
        memo_change[amount] = float("inf")
        return float('inf')
    elif amount > 0 and amount in coins:
        memo_change[amount] = 1
        return 1
    else:
        currentCoin = coins[0]
        if currentCoin > amount:
            memo_change[amount] = fast_change(amount, coins[1:])
            return memo_change[amount]
        else:
            useIt = 1 + fast_change(amount - currentCoin, coins[1:])
            loseIt = fast_change(amount, coins[1:])
            memo_change[amount] = min(useIt,loseIt)
            return memo_change[amount]
'''



def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    
    if (amount,tuple(coins)) in memo_change:
        return memo_change[(amount,tuple(coins))]
    elif amount == 0:
        return 0
    elif amount in coins:
        memo_change[(amount,tuple(coins))] = 1
        return 1
    elif coins == [] or amount < 0:
        return float("inf")
    else:
        useIt = 1 + fast_change(amount - coins[-1], coins)
        loseIt = fast_change(amount, coins[:-1])
        answer = min(useIt,loseIt)
        memo_change[(amount,tuple(coins))] = answer
        return answer

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(87, [5, 50, 20, 1, 100, 10]))
print(fast_change(234, [5, 50, 20, 1, 100, 10]))
print(fast_change(87, [1, 3, 7, 12]))

