#1Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

s = input()
pattern = re.compile('ab*')
match = pattern.match(s)
    
if match:
  print(match.group())
else:
  print("NO")

#2Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
  
import re

s = input()
pattern = re.compile('abb(b?)$')
match = pattern.match(s)
    
if match:
  print("Yes")
else:
  print("NO")
    

#3Write a Python program to find sequences of lowercase letters joined with a underscore.
  
import re
s = input()
x = re.findall(r'\b[a-z]+_[a-z]+\b', s)
print(x)
if x:
  print("Yes")
else:
  print("NO")
    


#4Write a Python program to find the sequences of one upper case letter followed by lower case letters.
  
import re
s = input()
x = re.findall(r'\b[A-Z][a-z]+\b', s)
print(x)
if x:
  print("Yes")
else:
  print("NO")

#5Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
  
import re
s = input()
x = re.findall(r'\Aa.+b\b', s)
print(x)
if x:
  print("Yes")
else:
  print("NO")
    

#6Write a Python program to replace all occurrences of space, comma, or dot with a colon.
  
import re
  
s = input()
x = re.sub(r'[ ,.]',':', s)
print(x)


#7Write a python program to convert snake case string to camel case string.

import re
  
s = input()
x = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), s)
print(x)

#8Write a Python program to split a string at uppercase letters.

import re
  
s = input()
x = re.findall('[A-Z][a-z]*', s)
print(x)

#9Write a Python program to insert spaces between words starting with capital letters.

import re
s = input()
x = re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
print(x)


#10Write a Python program to convert a given camel case string to snake case.
import re
  
s = input()
x = re.sub('([a-z])([A-Z])', r'\1_\2', s)
print(x.lower())
