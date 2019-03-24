#!/usr/bin/python
#attempt at fibonacci sequence function
def fibonacci(lst):
    while (len(lst) < 30):
        lst.append(lst[-2] + lst[-1])
    return lst
    
print(fibonacci([1, 1, 2]))