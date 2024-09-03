# 1. defining and calling a function- You define a function using
# the def keyword, followed by the function name and parentheses ()
#  which may include parameters. The function's code block is 
# indented below the definition.

def salamu(name="Guest"):
    print(f"hello, {name}")

# calling a function
salamu() 



# 2. Function parameters and arguments
#     Parameters: Variables listed inside the parentheses in the function definition.
#     Arguments: Values passed to the function when calling it.

# You can define functions with multiple parameters

def add(a, b):
    return a + b
result = add(5, 3)
print(result)


 
#  3. Default parameters
# You can provide default values for parameters, which are used if no argument is provided.

def salamu(name = "Guest"):
    print(f"Hello {name}")
salamu()



# 4. Keyword Arguments
# You can pass arguments by explicitly specifying the parameter name.

def personal_details(name, age):
    print(f"{name} is {age} years old")
personal_details(name="Anthony", age=29)



# 5. Variable-Length Arguments
# Use *args for a variable number of positional arguments and **kwargs for a variable 
# number of keyword arguments.

def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

print(multiply(2, 3, 4))  # Output: 24

def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)  


# 6. Lambda Functions
# Lambda functions are anonymous functions defined with the lambda keyword. They are
#  often used for short, throwaway functions.

add = lambda x, y: x + y
print(add(5, 3))  # Output: 8


# 7. You can add documentation to your functions using docstrings. These are placed immediately 
# after the function definition.

def square(x):
    """Returns the square of a number."""
    return x * x

print(square.__doc__)  # Output: Returns the square of a number.
