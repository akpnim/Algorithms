#recursive implementation with dictionary to cache subproblem outputs for fast lookup. 

import sys
import time 

a = time.time()

G = []
with open('ENTER FILE NAME','r') as file: 
    for line in file: 
        G.append([int(i) for i in line.split()]) #v = G[i][0] value and w = G[i][1] weight starting from i=1 
#G = [(6,4),(3,4),(2,3),(4,2),(4,3)] #test case 
W = G[0][0] #size
n = G[0][1] #number 
S = {}
ans = 0 
winner = 0  

sys.setrecursionlimit(10*n)

def recurknap(n,C):
    if n == 0: 
        return 0 #already computed above - basically all zeroes 
    
    if G[n][1] > C: 
        return recurknap(n-1,C)
    
    if (n-1,C) not in S: 
        S1 = recurknap(n-1,C)
        S[(n-1,C)] = S1
    else: 
        S1 = S[(n-1,C)]

    if (n-1,C-G[n][1]) not in S: 
        S2 = recurknap(n-1,C-G[n][1])
        S[(n-1,C-G[n][1])] = S2 
    else: 
        S2 = S[(n-1,C-G[n][1])]
    
    return max(S1,S2 + G[n][0])

print(recurknap(n,W))

b = time.time()

print(b-a,'s')

