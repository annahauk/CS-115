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
        use_it_weight = itemList[0][0]
        use_it_value = itemList[0][1]
        use_it_residual_value , use_it_residual_backpack_contents = knapsack(capacity-use_it_weight, itemList[1:])
        
        useIt = [use_it_value + knapsack(capacity - use_it_weight, itemList[1:])[0], [itemList[0]] + knapsack(capacity - itemList[0][0], itemList[1:])[1]]
        lose_it_residual_value, lose_it_residual_backpack_contents = knapsack(capacity, itemList[1:])
        max_value=max(use_it_residual_value,lose_it_residual_value)
        if max_value == use_it_residual_value:
            return [use_it_value+use_it_residual_value,[itemList[0]]+use_it_residual_backpack_contents]
        else:
            return [lose_it_residual_value, lose_it_residual_backpack_contents]

knapsack(6, [[1, 4], [5, 150], [4, 180]])
#[184, [[1, 4], [4, 180]]]

#[acc value,[items grabbed]]
