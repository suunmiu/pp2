
"""
You are given list of numbers separated by spaces. 
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
