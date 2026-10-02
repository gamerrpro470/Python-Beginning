history = []
def sum(a , b):
    return a + b 

# add = sum(12 , 4)

def minus(a , b):
    return a - b

# subtract = minus(10 - 7)

def multiplication(a , b):
    global history
    history.append((a , b))
    return a * b

# multiply = multiplication(12 , 4)

def division(a , b = 1):
    return a / b

# divide = division(12 / 2)

def operations(*args):
    return sum(args)

average = lambda a , b : (a + b) / 2

def factorial(n):
    if n == 0 :
        return 0
    return n * factorial(n -1)

