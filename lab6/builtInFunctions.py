'''
1. Write a Python program with builtin function to multiply all the numbers in a list
'''
import functools
a = [1, 2, 3, 4, 5]
print(functools.reduce(lambda x, y: x * y, a))

'''
2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
'''
s = str(input())
low = 0
up = 0
for i in s:
    if i.islower():
        low +=1
    if i.isupper():
        up +=1
print("lower case:", low, "upper case:", up)

'''
3. Write a Python program with builtin function that checks whether a passed string is palindrome or not.
'''
s = str(input())
t = s[::-1]
if t == s:
    print("palindrome")
else:
    print("not palindrome")

'''
4. Write a Python program that invoke square root function after specific milliseconds.
'''
import math
a = int(input())
b = int(input())
print(math.sqrt(a+b/1000))

'''
5. Write a Python program with builtin function that returns True if all elements of the tuple are true.
'''
a = (True, True, False)
b = (True, True, True)
print(all(a))
print(all(b))
