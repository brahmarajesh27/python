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
        print('Solution' +str(sol)+ str(itr) +'\n')
        print("\n".join('o'*i +'Q'+'o'* (N-i-1) for i in itr)+"\n\n\n\n")
        break

             
        
                                                
                                              
                                              
    
   
                                             
                                             
