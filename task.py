# Factorial yarad


def factorial(f):
    if f == 0:
        return 1
    else:
        return f * factorial(f-1)
    


print(factorial(5))

