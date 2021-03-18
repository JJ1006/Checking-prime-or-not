import math
num=float(int(input()))
c=math.sqrt(num)
for i in range(2,int(c)):
    if num%i==0:
        print("The number is NOT PRIME")
        break
else:
        print("The number is PRIME")