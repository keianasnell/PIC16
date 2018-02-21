import time

N = 100000 #a very large integer
total = 0

#original function to generate array of squares
def f(x):
    return x**2

def func0():
    x = range(N)
    y = []
    t1 = time.clock()
    for i in x:
        y.append(f(i))
    t2 = time.clock()
    total = (t2-t1)
    print total
    return y

#Write a lambda function g that accomplishes f's task
g = lambda a: a**2

#case 1: use g()
def func1():
    total = 0
    x = range(N)
    z = []
    t1 = time.clock()
    for i in x:
        z.append(g(i))
    t2 = time.clock()
    total = (t2-t1)
    print total
    return z
    
#case 2: do not use g() or f()
def func2():
    total = 0
    a = range(N)
    b = []
    t1 = time.clock()
    for i in a:
        b.append(i**2)
    t2 = time.clock()
    total = (t2-t1)
    print total
    return b

#case 3: initialize y to range(N) then square the elements in place
    #is it more efficient to reuse an existing list (if possible)
def func3():
    total = 0
    y = range(N)
    t1 = time.clock()
    for i in y:
        y[i] = y[i]**2
    t2 = time.clock()
    total = (t2-t1)
    print total
    return y


#case 4: use list comprehension to generate list of squares
total = 0
t1 = time.clock()
squares = [g(num) for num in range(N)]
t2 = time.clock()
total = (t2-t1)
print total

#case 5: use map to generate list of squares
def square(x):
    return x**2
total = 0
t1 = time.clock()
c = map(square, range(N))
t2 = time.clock()
total = (t2-t1)
print total

