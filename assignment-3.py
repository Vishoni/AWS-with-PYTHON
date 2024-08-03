# Function to replicate built-in sum()
def custom_sum(iterable, start=0):
    total = start
    for item in iterable:
        total += item
    return total

# Function to replicate ljust() and rjust()
def custom_ljust(s, width, fillchar=' '):
    if len(s) >= width:
        return s
    else:
        return s + fillchar * (width - len(s))

def custom_rjust(s, width, fillchar=' '):
    if len(s) >= width:
        return s
    else:
        return fillchar * (width - len(s)) + s

# Function to find Palindrome
def is_palindrome(s):
    return s == s[::-1]

# Function to generate Fibonacci sequence up to n
def fibonacci(n):
    fib_seq = []
    a, b = 0, 1
    while a < n:
