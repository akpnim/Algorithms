#In the section of the original ksaraju that was coded up to find the size of each SCC, we need to add the below condition: 
#if int(-1*vertex) in A: 
    #reutrn "Unsatisfiable"
#key idea is to get an implication graph from the given vertex set 
#will add a function in the beginning to convert the edges into an implication graph  

import numpy as np
import sys
from collections import Counter
sys.setrecursionlimit(900000)

#x = 8 
x = 1000000 # number of variables and clauses is the same and it is this 

def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(5)

def list_from_txt (address):
    A =[]
    with open (address,'r') as file: 
        for line in file: 
         a = [int(i) for i in line.split()]
         A.append(a)
    return A

def implist_from_txt (address):
    A =[]
    with open (address,'r') as file: 
        for line in file: 
            a = [int(i) for i in line.split()]
            if len(a) > 1:
                imp1 = [int(-1*a[0]),a[1]]
                imp2 = [int(-1*a[1]),a[0]]
                A.append(imp1)
                A.append(imp2)
    return A
    
def invert_list_in_list (A):
    B=[]
    for element in A:
       B.append(element[::-1])
    return B

def edge_list_to_vertex (C,n=x): #n is set as number of vertices 
    D = {i+1:[i+1] for i in range(-n-1,n)}
    for [i,j] in C:
        if j not in D[i]:
            D[i].append(j) 
    del D[0]
    return D 

explored = {i+1:False for i in range(-x-1,x)}
T = {i+1:0 for i in range(-x-1,x)}
S = []
too_sat = {i+1:[] for i in range(-x-1,x)}
t = 0
s = 10000000000000000

def DFS(G,i):
    explored.update({i:True})
    if i in G:
        for j in G[i]:
            if explored[j]==False:
                DFS(G,j)
    global t
    t = t + 1
    T[i] = t

def DFS_two(G,i):
    explored.update({i:True})
    too_sat[s].append(i)
    for j in G[i]:
        if explored[j]==False:
            DFS_two(G,j)
    print ("s2 = ",s)
    S.append(s)


def DFS_loop(G):
    i = x 
    global explored
    global T 
    while i>-x:
        if explored[i]==False:
            DFS(G,i) #failing at i= 874931; [874931,272792]
        i = i-1
    del T[0]
    return T 

def DFS_loop_two(G,B=[]):
    global explored
    explored = {i+1:False for i in range(-x-1,x+1)}
    global S 
    S = []
    for i in B:
        if explored[i]==False:
            global s 
            s = i
            print ("s=",s)
            DFS_two(G,s) #failing at i= 874931; [874931,272792]
    return S 

def sortout_T(A: dict):
    tupdic = []
    for key in A: 
        tupdic.append((A[key],key))
    scores = sorted(tupdic)[::-1]
    scores = [j[1] for j in scores]
    return scores 

def main():

    G_list = implist_from_txt(ENTER FILE NAME)
    G_list_trans = invert_list_in_list(G_list)
    G_trans = edge_list_to_vertex(G_list_trans)
    G_regular = edge_list_to_vertex(G_list)
    Z = DFS_loop(G_trans)
    print(Z[1])
    print ("first run complete!")
    i = len(Z)
    print(i)
    P = sortout_T(Z)
    print(P[0:100])
    print ("descending order done!")
    #print("descending order T = ",P)
    jawab = DFS_loop_two (G_regular,P) #returns the list of source vertices 
    jawab = [i for i in jawab]
    print ("jawab computed")
    print(most_frequent(jawab))
    print(len(too_sat[33604]))
    #print(len(too_sat[970627]))
    for key in too_sat:
        checker = set(too_sat[key])
        for element in too_sat[key]: 
            if int(-1*element) in checker: 
                print(element)
                print("unsatisfiable") 
                exit()
    print ("satisfiable")

main()

