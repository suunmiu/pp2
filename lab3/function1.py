
"""
1.A recipe you are reading states how many grams you need for the ingredient. 
Unfortunately, your store only sells items in ounces. Create a function to convert
grams to ounces. ounces = 28.3495231 * grams

"""
grams = 5
def my_function(x):
  print(28.3495231 * x)
my_function(grams)

"""
2.Read in a Fahrenheit temperature. 
Calculate and display the equivalent centigrade temperature.
 The following formula is used for the conversion: C = (5 / 9) * (F – 32)

"""
F = 95
def my_function(x):
  print((5/9)*(x-32))
my_function(F)
"""
3.Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm.
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


"""
4. You are given list of numbers separated by spaces. 
Write a function filter_prime which will take list of numbers as an agrument and returns only 
prime numbers from the list.


"""
nn = [1, 2, 3, 4, 5, 6]
def filter_prime(num):
    i = 1
    count = 0
    while i < num:
       if(num % i ==0):
           count+=1
       i+=1
    if (count == 0):
        print(num)
      
j=0        
while j < len(nn):
    filter_prime(nn[j])

"""
5.Write a function that accepts string from user and print all permutations of that string.

"""
s = str(input())
def permutation(st):
    t = ""
    for x in st:
        if x != " ":
            t = t + x
    print(t)

permutation(s)

"""
6.Write a function that accepts string from user, return a sentence with the words reversed. 
We are ready -> ready are We
"""
def reverse(st):
    st = st[::-1]
    words = st.split()
    t = ""
    for word in words:
        word = word[::-1]
        t = t + word + " "
        
    print(t)

s = str(input())
reverse(s)

"""
7.Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
"""
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] == '3':
            return True
    return False

numbers = input()
numbers = numbers.split()
print(has_33(numbers))

"""
8.Write a function that takes in a list of integers and returns True if it contains 007 in order
"""
def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == '0' and nums[i+1] == '0' and nums[i+2] == '7':
            return True
    return False

numbers = input()
numbers = numbers.split()
print(spy_game(numbers))

"""
9. Write a function that computes the volume of a sphere given its radius.

"""
def volume(radius):
    print((4/3) * 3.14 * radius * radius * radius)

r = int(input())
volume(r)

"""
10.Write a Python function that takes a list and returns a new list
 with unique elements of the first list. Note: don't use collection set.

"""
def unique_list(nums):
    unique = []
    for i in nums:
        if i not in unique:
            unique.append(i)
    return unique
    
numbers = input()
numbers = numbers.split()
print(unique_list(numbers))

"""
11.Write a Python function that checks whether a word or phrase is palindrome or not.
 Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam


"""
def palindrome(str):
    t = str[::-1]
    if t == str:
        print("Yes")
    else:
        print("No")
    
s = input()
palindrome(s)

"""
Define a functino histogram() that takes a list of integers and prints a histogram to
 the screen. For example, histogram([4, 9, 7]) should print the following:

"""
def histogram(nums):
    for x in nums:
        print('*' * int(x))
    
numbers = input()
numbers = numbers.split()
histogram(numbers)
            
"""
13.Write a program able to play the "Guess the number" - game, 
where the number to be guessed is randomly chosen between 1 and 20. 
This is how it should work when run in a terminal:

"""
import random
def play():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name},I am thinking of a number between 1 and 20.")

    number = random.randint(1, 20)
    guesses = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            break

    print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
    
play()

"""
14.
Create a python file and import some of the functions from the above 13 tasks and try to use them.

"""
from function1 import is_prime, reverse, play

play()
is_prime(5)
t = str(input())
reverse(t)