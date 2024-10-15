class Value_too_large(Exception):
    pass


def factorial(n):
    if n > 5000:
        raise Value_too_large("Value too large")
    
    if n == 0:
        return 1
    
    else:
        try:
            return n * factorial(n - 1)
    
        except Value_too_large as ve:
            print(ve)
    
print(factorial(5000))