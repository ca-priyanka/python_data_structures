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
