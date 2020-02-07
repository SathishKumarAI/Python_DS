# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 09:18:40 2020

@author: Administrator
"""

def lis(ar,n):
    l=[1]*n
    
    for i in range(n):
        for j in range(i):
            if( ar[i] > ar[j] and l[i] < l[j] +1):
                l[i] = l[j] + 1   
        print(l)
    return max(l)


a=[10,22,9,33,21,50,41,60]

n=8
s=lis(a,n)
print(s)
            
    