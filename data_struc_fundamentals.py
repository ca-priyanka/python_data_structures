# write a script that prompts the user for their phone number, x. Then carry out the following steps:
# 1. Compute x minus the sum of the digits of x. Call this result y. (hint: to find the sum of the digits of x, check to see what x//10 and x%10 give you)
# 2. Compute the sum of the digits of y, and store the result back in y.
# 3. Repeat step 2 until y has just one digit, then display it.

def sum_of_digits(x):
    total = 0
    while x > 0:
        total+= x % 10
        x //= 10
    return total

def step_two(n):
    while n >= 10:
        n = sum_of_digits(n)
    return n

def step_one(x):
    y = x -sum_of_digits(x)
    y = step_two(y)
    return y

def main():
    try:
        x = int(input("Enter your phone number:"))
        if x <= 0:
            print(" Enter positive number")
            return
        result = step_one(x)
        print(result)
    except ValueError:
        print("invalid input")

# Test Cases # enter 9 for algorithmic behaviour
def run_tests():
    test_cases = [
        (4120512344, 9),
        (5641235474, 9),
        (5464, 9),
        (123,9),
        (11,9),
        (9,9),
        (999,9)
    ]
    for num, expected in test_cases:
        result = step_one(num)
        print(f"{result}")

# Run the program
if __name__ == "__main__":
    run_tests() # first run test cases

    main() # Then run interactive program