'''
Anna Hauk
I pledge my honor that I have abided by the Stevens Honor System.
Cs115 Lab 4
'''

def knapsack(capacity, itemList):
    '''returns list of maximum value and list of items that achive the
greatest value without exceeding capacity'''
    if itemList == []:
        return [0,[]]
    if capacity == 0:
        return [0,[]]
    elif itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    else:
        useIt = [itemList[0][1] + knapsack(capacity - itemList[0][0], itemList[1:])[0], [itemList[0]] + knapsack(capacity - itemList[0][0], itemList[1:])[1]]
        loseIt = knapsack(capacity, itemList[1:])
        return max(useIt,loseIt) #can take max of lists,  reads element by element 

