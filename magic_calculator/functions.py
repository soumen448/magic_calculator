def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    try:
        res = a/b
    except ZeroDivisionError:
        print("Division by 0 is not allowed")
        print("The denominator is approximated as 10^-10")
        res = a/10**(-10)
    finally:
        return res