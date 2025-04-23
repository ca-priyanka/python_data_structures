## Chapter 1
# 1.Sample Program for heart rate:

age = int(input('Enter your age in years: '))
max_heart_rate = 206.9 - (0.67 * age) # as per Med Sci Sports Exerc.
target = 0.65 * max_heart_rate
print(f"Your target fat-burning heart rate is ,{target}")

# 2.Raising error and exception handling:

import collections
from optparse import Values

def sum(values):
    if not isinstance(Values, collections.Iterable):
        raise TypeError('Parameter must be an iterable type')
    total = 0
    for v in values:
        if not isinstance(v, (int, ﬂoat)):
            raise TypeError('elements must be numeric')
        total = total+ v
    return total

## test print(sum(3,6,3,4))

# 3.Exception Handling
age = int(input("Enter your age in years: "))

#an initially invalid choice -20
while age <= 0:
    try:
        age = int(input('Enter your age in years: '))
        if age <= 0:
            print('Your age must be positive')
    except ValueError:
            print('That is an invalid age specification')
    except EOFError:
        print('There was an unexpected error reading input.')
        raise # lets reraise this exception

#4. Iterator, lazy evaluation
for j in range(10):
    print(j)

# list(id.values())
# Define a dictionary
student = {
    "name": "Alice",
    "age": 21,
    "grade": "A"
}

if 21 in student.values():
    print("Age 21 exists in the dictionary!")

for value in student.values():
    print(value)


prices = {"apple": 1.0, "banana": 0.5, "orange": 0.75}
price_list = list(prices.values())  # [1.0, 0.5, 0.75]

# 5. Generator
    # The generator object is not executed until you iterate over it.
    # To get the factors, you must consume the generator by:
    #     Looping over it (for loop)
    #     Converting it to a list (list())
    #     Manually fetching values with next()

def factors(n): # traditional function that computes factors
    results = [ ] # store factors in a new list
    for k in range(1,n+1): # divides evenly, thus k is a factor
        if n % k == 0:
            results.append(k) # add k to the list of factors
    return results # return the entire list

# 6. In contrast, an implementation of a generator for computing those 
# factors could be implemented as follows:
def factors(n): # generator that computes factors
    for k in range(1,n+1): # divides evenly, thus k is a factor
        if n % k == 0:
            yield k  # yield this factor as next result

print(list(factors(456)))

for factor in factors(114):
    print(factor, end=" ")

gen = factors(38)
print(next(gen))  # 1
print(next(gen))  # 2
# ... until StopIteration is raised

# 7. compute factors of a number n
def factors(n):
    k = 1
    while k*k < n:
        if n%k == 0:
            yield k
            yield n //k
        k+=1
    if k*k == n : # special case if n is a perfect square
        yield k
    
print(list(factors(32)))

# 8. first n nos of fibonacci series
def fibonacci(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        yield a
        next = a+b
        a= b
        b= next
        count += 1

print(list(fibonacci(10)))

# 9. Conprehension Syntax:
def squares(n):
    return [k*k for k in range(1,n+1)] 
    
print(squares(5))

# 10. Simultaneous Assignments - simplifies the presentation of the code:
j, k = 5, 7
j,k = k,j

# Simultaneous assignment + generator implementation:
def fibonacci(x):
    a,b = 0,1
    count = 0
    while count < x:
        yield a
        a,b = b, a+b
        count +=1

print(list(fibonacci(15)))

def fib(y):
    a,b = 0,1
    for _ in range(y):
        yield a
        a,b = b, a+b

print(list(fib(15)))


