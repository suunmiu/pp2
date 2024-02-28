#1

import math
p = math.pi
print("import degree")
a = int(input())
print("output radian", a* p/180)

#2
import math
a= int(input())
b= int(input())
c= int(input())
print((c+b)/2 *a)

#3
import math
n = int(input())
l = int(input())
p = math.pi
a = l/2 * math.tan((n - 2)*p/n/2)
print(math.ceil(n*l*a/2))


#4
import math
l = int(input())
h = int(input())
print(l*h)