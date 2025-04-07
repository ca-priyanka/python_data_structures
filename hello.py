print("hello")
def my_function():
    print("Hello from my Function")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a,b):
    return a+b

#call functions
my_function()

my_function_with_args("Pri", "good luck")

x = sum_two_numbers(7,9)
print(x)

# function to return a list of strings
def list_benefits():
    return["more organized code", "more readable code", "easier code reuse", 
           "allowing programmers to share and connect code together"]

def build_sentence(benefit):
    return"%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()