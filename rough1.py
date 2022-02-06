import math
import inspect
from inspect import signature
import random

list_fun = dir(math)

list_fun = list_fun[5:]
print(list_fun)

for i in list_fun:
    try:
     fun = getattr(math,i)
     
     sig = signature(fun)

     if len(str(sig))==6:
        try:
         print(f"The function is {i}")
         print("\n\n")
         print(f"************What the function does?*****************\n\n")
         print(inspect.getdoc(fun))
         print("\n\n")
         a = random.uniform(0,1)
         print(f"\n{i}({a}) is \n")
         print(fun(a))
         print("<><>"*40+"\n\n")
        except ValueError:
            a = random.randint(1,5)
            print(f"\n{i}({a}) is \n")
            print(fun(a))
            print("<><>"*40+"\n\n")
            
     else:
         print(f"The function is {i}")
         print("\n\n")
         print(f"************What the function does?*****************\n\n")
         print(inspect.getdoc(fun))
         print("\n\n")
         c ,d = random.randint(1,4),random.randint(1,4)
         print(f"The arguments are a = {a} and b = {b}")   
         print(f"\n{i}({a},{a}) is \n")
         print(fun(c,d))
         print("<><>"*40+"\n\n")
         
     
    except :
        print("\n")
