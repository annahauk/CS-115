'''
Anna Hauk
I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 4 
'''
from cs115 import *

memo = {}

def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if n in memo:
        return memo[n]
    if n == 0:
        memo[0]=2
        return 2
    if n == 1:
        memo[1] =1
        return 1
    one = fast_lucas(n-1)
    two = fast_lucas(n-2)
    memo[n-1] = one
    memo[n-2] = two
    return one + two

memo_change = {}    
def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    if amount in memo_change:
        return memo_change[amount]
    if amount==0:
        return 0
    elif coins==[] or amount < 0:
        return float('inf')
    else:
        lose_it_result = fast_change(amount, coins[1:])
        use_it_result = fast_change(amount-coins[0],coins)
        answer = min(lose_it_result, 1 + use_it_result)
        memo_change[amount]=answer
        return answer

    ''''

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

'''
    #attempt 3
'''memo_change = {}    
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
        '''

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))
