# -*- coding: utf-8 -*-

a=3+1j;
b=4+8j;
c=[2,1,3,5,7]
d = (a+b);

if a !=3+1j:
    #indentation is important (substitute of{})
    print("asd")
    #elif can be used insted of else if
    

else:
    print("obviously")

    
y=1 if a!=0 else -1
print(y)
def funza2(t):
    global y
    #declare the variable y as a reference to the global variable
    y = 3
    print("sono funza2",y,t)
#function definition
def funza(x):
    
    funza2(3)

funza(1)
print(y)

import math
#including libraries
math.log(math.e)
#accessing methods and variables inside a library
# it is possible to import single variables and methods 'from math import log,e'
#from math import log as take_logarithm
#common conventions: import numpy as np, import pandas as pd, import pylab as plt

# %%
for x in c:
    print(x)
x=0
i=0
while x !=7:
    x=c[i]
    print(x)
    i=i+1
str="aosidjoiasjdoijo"
f=[1,'s','adfs',4,5]

# %%

