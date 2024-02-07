
"""
Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm.
 How many rabbits and how many chickens do we have? 
 create function: solve(numheads, numlegs):

"""
heads = 35
legs = 94
def solve(numheads, numlegs):
    """
    x + y = 35
    2x + 4 y= 94
    """
    chickens = (numheads*4 - numlegs)/2
    rabbits = (numlegs - numheads*2 )/2
    print(chickens, rabbits)

solve(heads , legs)
