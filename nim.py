'''
Anna Hauk
I pledge my honor that I have abided by the Stevens Honor System.
CS 115
HW 11
'''


# nim template DNaumann (2018), for assignment nim_hw11.txt 

# Global variables used by several functions
piles = []  # list containing the current pile amounts
numPiles = 0  #number of piles, which should equal len(pile)
coins = 0   #number of coins per pile


def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    print("We're going to play Nim.  You'd better play optimally or I'll win.")
    init_piles()
    while True:
        # uncomment the suggest() routine here to help you
        # win the game as the non computer player
        
        # suggest()
        
        user_plays()
        display_piles()
        if sum(piles) == 0:
            print("You won")
            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:
            print("I win ... AGAIN")
            break


def init_piles():
    """ Assign initial values to the global variables 'coins' and 'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global coins
    global numPiles
    
    numPiles = int(input("Enter a number of piles: "))
    while numPiles <= 0 :
        numPiles = int(input("Enter a number of piles: "))
    for i in range(numPiles):
        piles.append(0)
    for i in range(numPiles):
        coins = int(input("Enter number of coins for pile " + str(i) + ": "))
        while coins < 1:
            coins = int(input("Enter number of coins for pile " + str(i) + ": "))
        piles[i] = coins
    display_piles()

        
def display_piles():
    """ display current amount in each pile """
    global piles
    global numPiles
    
    for i in range(numPiles):
        print("pile " + str(i) + " = " + str(piles[i]))


def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt
    
def get_pile():
    """ return user's choice of pile. Keep prompting until the choice is valid, i.e.,
        in the range 0 to numPiles - 1. """
    global piles
    global numPiles
    
    currPile = int(input("Choose a pile: "))
    while currPile < 0 or currPile > numPiles - 1:
        currPile = int(input("Choose a pile: "))
    return currPile

def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles
    grab = int(input("How many coins? "))
    while grab > piles[pnum] and grab <= 0 :
        grab = int(input("How many coins? "))
    return grab


def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global numPiles
    total = 0
    for i in range(numPiles):
        total ^= piles[i]
    return total

def suggest():
    """ as the player, get suggestions for 
        the move to make to win """
    p,n = opt_play()
    print("choose pile " + str(p) + " and remove " + str(n) + " coin(s)")

def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global numPiles
    
    # Step 1: compute the bitwise exclusive-or of A, B, and C.  Call this the "nim-sum" of the game.  
    # Step 2: compute the bitwise exclusive-or of the nim-sum with each pile individually. Call each of these the pile-sums.
    # Step 3: If some pile-sum is smaller than the number of coins in that pile, then the optimal play
    #         is to remove coins from that pile; remove as many coins as necessary to
    #         reduce the pile to its pile-sum.
    #         else if no pile-sum smaller than number of coins in then pile, then
    #         just remove a single coin from the first non-zero size pile

    nim_sum = game_nim_sum()
    for i in range(numPiles):
        num_coins_in_pile_i = piles[i]
        if num_coins_in_pile_i == 0:
            continue
        pile_sum = num_coins_in_pile_i ^ nim_sum

        if pile_sum < num_coins_in_pile_i:
            return (i,num_coins_in_pile_i-pile_sum)
    # if we reach here, it means that no pile sum was
    # smaller than its pile sum, so just find the first
    # non-zero pile and remove a single coin from it
    for i in range(numPiles):
        num_coins_in_pile_i = piles[i]
        if num_coins_in_pile_i > 0:
            return (i,1)


def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played
        Implement this using opt_play(). """
    global piles
    print("My turn ... prepare to be dazzled!!!")
    p,n = opt_play()
    piles[p] = piles[p] - n
    print("I remove " + str(n) + " from pile " + str(p))
    
#   start playing automatically
if __name__ == "__main__" :
    play_nim()