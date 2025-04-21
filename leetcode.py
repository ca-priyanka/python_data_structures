# first n numbers of fibonacci sequence


def fib_sequence(n):
    f = [1,2]
    while len(f) < n:
        num = f[-1] + f[-2]
        f.append(num)
    return(f)

#test case 1
n = 15
x = fib_sequence(n)
print(x)


# test case 2
n = 7
y = fib_sequence(n)
print(y)


# sum of 5 nos
def sum_nos(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return(sum)
   
x = sum_nos([1,2,3,4,5,6])
print(x)

z = [5,6,7,8,9,5,4,3]
a= sum_nos(z) 
print(a)

# First n prime numbers
def is_prime(num):
    if num <=1:
        return False
    for i in range(2, int(num**0.5)+1): # calculate square root of num and check factors up to the sqrt
        if num % i == 0:
            return False
    return True

def prime_factor_list(n):
    primes = []
    fac = 2
    while len(primes) < n:
        if is_prime(fac):
            primes.append(fac)
        fac += 1
    return primes

# function call
n = 15
print("first", n, "prime nos are",prime_factor_list(n))


# Write a script to compute how many unique prime factors an integer has. 
#  For example, 12 = 2 x 2 x 3, so has two unique prime factors, 2 and 3. 
# Use your script to compute the number of unique prime factors of 1234567890.
def prime_factor_count(n):
    if n <=1:
        return 0
    count = 0
    divisor =2

    while divisor * divisor <= n:
        if n % divisor == 0:
            count += 1
            while n % divisor == 0:
                n = n // divisor
        divisor += 1

    if n > 1:
        count += 1
    return count

# function call
number = 1234567890
unique_factors = prime_factor_count(number)
print(unique_factors)
        