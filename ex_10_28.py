#exercise 1
#what is decorator in python?
#Think : how to caculate a program's execute time?
#Maybe you use this way:

import time
def bar(*args,**kwargs):
    start = time.time()
    print(sum(args))
    print(time.time()-start)
# bar(5,7,10)

#But when you want to define another function,and still want to caculate the run time
#you have to wirte those two line again
#Decorator can help you to deal with this problem

# Define Decorator
# the param in Decorator is a function Object
# Decorator's return value is a function
def time_calc(func):
    def wrapper(*args, **kargs):
        print("use decorator")
        start_time = time.time()
        f = func(*args, **kargs)
        exec_time = time.time() - start_time
        return f
    return wrapper
#After defining a decorator to record the execute time ,you can know every function's execute time by adding
#a symbol "@Decorator" before define the function,it means this function needs the decorator to enrich the function

# use decorator
@time_calc
def add(a, b):
    return a + b

@time_calc
def sub(a, b):
    return a - b

#Now,you get the jounior method to define a simple decorator!

