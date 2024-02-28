#1

n = int(input())
for i in range(n):
  print(i*i)


#2
n = int(input())
even_numbers = [str(i) for i in range(n + 1) if i % 2 == 0]
result = ', '.join(even_numbers)
print( result)


#3
def div34(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
result = list(div34(n))
print(result)


#4
def sqrs(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = int(input())
b = int(input())
for i in sqrs(a, b):
    print(i)

#5
 
def count(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for i in count(n):
    print(i)
   