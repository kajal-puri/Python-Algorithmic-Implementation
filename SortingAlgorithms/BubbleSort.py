# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 19:25:11 2016

@author: kajal
"""

def bubblesort (List):
    for i in range (len (List)):
        for k in range (len (List)-1, i, -1):
            if (List[k]<List[k-1]):
                swap(List,k,k-1)
def swap(List,x,y):
    tmp=List[x]
    List[x]=List[y]
    List[y]=tmp
List1=[1,100,3,9,0,1,23,42,11]
bubblesort(List1)
print(List1)
        