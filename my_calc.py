def plus(x):
    print(type(x))
    return sum(x)
w = plus ([4, 5, 6])
print(w)

def minus(a, b):
    return a - b
w = minus (4, 5)
print(w)

def mult(a, b):
    return a * b
w = mult (4, 5)
print(w)

def div(a, b):
    if b !=0:
        return a / b
    else:
        print('do not do it')
