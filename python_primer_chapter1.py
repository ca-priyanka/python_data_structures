#R-1.1 Write a short Python function, is multiple(n, m), that takes
# two integer values and returns True if n is a multiple of m, that 
# is, n = mi for some integer i, and False otherwise.

def is_multiple(n,m):
    if n % m == 0:
        return True
    else:
        return False
    
#print(is_multiple(23252,3))

#R-1.2 Write a short Python function, is even(k), that takes an 
# integer value and returns True if k is even, and False otherwise. 
# However, your function cannot use the multiplication, modulo, or 
# division operators.

def is_even(k):
    even = [2,4,6,8,0]
    for _ in range(k+1):
        if int(str(k)[-1]) in even:
            return True
        else:
            return False
        
#print(is_even(32326))

#R-1.3 Write a short Python function, minmax(data), that takes a 
# sequence of one or more numbers, and returns the smallest and 
# largest numbers, in the form of a tuple of length two. Do not use 
# the built-in functions min or max in implementing your solution.

def minmax(data):
    num = []
    for d in range(1,data+1):
        num.append(d)
    #tup = num[0], int(str(num)[-2])
    tup = num[0], (num)[-1]
    return tup
    
#print(minmax(950))

#R-1.4 Write a short Python function that takes a positive integer n
#  and returns the sum of the squares of all the positive integers 
# smaller than n.

def input(n):
    k = 1
    sum = 0
    while k < n:
        sum += k*k
        k += 1
    return sum

#print(input(5))

#R-1.5 Give a single command that computes the sum from Exercise 
# R-1.4, relying on Python’s comprehension syntax and the built-in 
# sum function.

def input(n):
    sum_sq = sum(i*i for i in range(n))
    return sum_sq

#print(input(4))

#R-1.6 Write a short Python function that takes a positive integer n and
# returns the sum of the squares of all the odd positive integers 
# smaller than n.

def input(n):
    k= 1
    odd = [1,3,5,7,9]
    sum = 0
    while k<n:
        if int(str(k)[-1]) in odd:
            sum += k*k
            k+=2
    return sum

#print(input(568))

#R-1.7 Give a single command that computes the sum from Exercise 
# R-1.6, relying on Python’s comprehension syntax and the built-in
# sum function.
def input(n):
    if n % 2 == 0:
        sum_sq = sum(i*i for i in range(1,n,2))
    else:
        sum_sq = sum(i*i for i in range(1,n-1,2))
    return sum_sq

#print(input(569))

#R-1.8 Python allows negative integers to be used as indices into a 
# sequence,such as a string. If string s has length n, and expression
# s[k] is used for index −n ≤ k < 0, what is the equivalent index j
# ≥ 0 such that s[j] references the same element?