# Int-to-Str Code Wars
# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?
# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# 100 --> "-100"

def number_to_string(num):
    result = str(num)
    return result

    """
    _summary_
    User calls function with an argument integer. The function converts the argument integer into a string with the Python native function str(), this is put in a variable called result.
    The function returns the variable result. to see the result the usre would have to print the result. print(number_to_string(42)) will print 42 but as a string. Allowing the user to 
    concatenate the intiger. print('my favorite number is ' + number_to_string(42))
    """