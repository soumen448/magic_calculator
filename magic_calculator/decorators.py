import random
import functions as f
def magic(a,b):
    num = random.rarandint(1,4)
    if num == 1:
        return f.add(a,b)
    elif num == 2:
        return f.sub(a,b)
    elif num == 3:
        return f.mult(a,b)
    elif num == 4:
        return f.div(a, b)