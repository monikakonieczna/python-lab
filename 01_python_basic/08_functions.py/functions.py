# There are mainly two types of functions in Python
# Built-in library function: There are standard functions in Python that are available to use.
# User-defined function: We can create our own functions based on our requirements. 

# Function to check whether x is even or odd
def evenOdd(x):
    if(x % 2 == 0):
        print("even")
    else:
        print("odd")
        
# Driver code to call the function
evenOdd(2)
evenOdd(15)