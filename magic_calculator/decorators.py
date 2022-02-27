import random
import magic_calculator.functions as f
def magic(a,b):
    num = random.randint(1,4)
    if num == 1:
        print("Magic Operation: Addition")
        return f.add(a,b)
    elif num == 2:
        print("Magic Operation: Subtraction")
        return f.sub(a,b)
    elif num == 3:
        print("Magic Operation: Multiplication")
        return f.mult(a,b)
    elif num == 4:
        print("Magic Operation: Division")
        return f.div(a, b)