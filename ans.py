# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:27:57 2018

@author: Jameer
"""

import numpy as np
import matplotlib.pyplot as plt
import math

alpha = [7,5,3]

l1=[]
l2 = []
for a in alpha :
        print(a)
        n = np.random.normal(a, 2*np.sqrt(2*np.log(2)), 1000)
        l1.append(n)
        plt.hist(n)
        plt.show()
for a in alpha :
        print(a)
        p=np.random.poisson(a,1000)
        
        l2.append(p)
        plt.hist(p)
        plt.show()
        


l3=[]
l4=[]

for i in range (3) :
    for j in range (1000) :
        l3.append(l1[i][j])
        
        
for i in range (3) :
    for j in range (1000) :
        l4.append(l2[i][j])
        
        

def poission(a,x) :
    return np.exp(-a)*np.power(a,x)/math.factorial(x)


sigma = [5 , 6 , 8]

def normal(m,v,x) :
    return 1/(v * np.sqrt(2 * np.pi)) * np.exp( - (x - m)**2 / (2 * v**2) )

for j in range (100) :
    for i in alpha :
        a = np.random.choice(l3,100)
        x = np.mean(a)
        y = poission(x,i)
        n, bins, patches = plt.hist([x, y])    
plt.show()       
        




for j in range (100) :
    for i in range (3) :
        b = np.random.choice(l4,100)
        m=alpha[i]
        v=sigma[i]
        x = np.mean(b)
        y = normal(m,v,x)
        n, bins, patches = plt.hist([x, y])
plt.show()        



