import math

print ("Enter the a number")
number = int(input())

primes = []
for i in range(2,number+1):
    primes.append(i)

i = 2
#from 2 to sqrt(number)
while(i <= int(math.sqrt(number))):
    if i in primes:
        for j in range(i*2, number+1, i):
            if j in primes:
                primes.remove(j)
    i = i+1

print (primes)