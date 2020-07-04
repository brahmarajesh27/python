# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 00:15:31 2020

@author: 717680
"""
from itertools import permutations
N=8

sol=1
COL= range(N)
for itr in permutations(COL):
    if N==len(set(itr[i]+i for i in COL))==len(set(itr[i]-i for i in COL)):
        print(str(itr) +'\n')
        break

             
        
                                                
                                              
                                              
    
   
                                             
                                             
