#You should output the sizes of the five largest SCCs in the given graph!
#The file contains the edges of a directed graph. Vertices are labelled as positive integers from 1 to 875714. 
#Part 1 of the code deals with converting a list of edges into adjacency lists for both graph and graph transpose. 
#Part 2 of the code deals with running depth-first search on Graph-transpose and getting runtimes T of each vertex in a new...
#...list T such that T[i-1] denotes the vertex. The list is sorted out in descending order of indices using argsort(which is a type of indirect sort) 
#Part 3 of the code deals with running depth-first search on the original graph in descending order of indices of max vertices in T. The output is...
#...a list of ''leader'' vertices for each vertex in the graph. 
#Part 4 deals with printing out the list of the 5 most frequently appearing leaders. 

#Here is a list of special functions invoked to perform interesting things- aka learning outcomes! 
#(a) argsort from numpy was used to perform an indirect sort on T using quicksort(default) in descending order 
#(b) Counter from collections was used to create a dictionary with the elements of the list as the key and their frequency as value. 
#(c) counter.most_common(5) was used to output the keys for the highest five values in the counter dictionary.
#(d) the recursion limit was increased because the size of the graph is ginormous. 
#(e) declaring and managing global variables - especially in local spaces is very important. 
#(f) PRACTICE THE ALGORITHM MANUALLY ON PAPER ON TEST CASES IS KEY TO A DEEPER UNDERSTANDING. 

import numpy as np
import sys
from collections import Counter
sys.setrecursionlimit(900000)

x = 875714 #enter the number of vertices in your graph input

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
    
def invert_list_in_list (A):
    B=[]
    for element in A:
       B.append(element[::-1])
    return B

def edge_list_to_vertex (C,n=x): #n is set as number of vertices 
    D = [[i+1] for i in range(n)]
    for [i,j] in C:
        D[i-1].append(j)
    return D 

explored = {i+1:False for i in range(x)}
T = [0 for i in range(x)]
S = []
t = 0
s = 10000000000000000

def DFS(G,i):
    explored.update({i:True})
    for j in G[i-1][1::]:
        if explored[j]==False:
            DFS(G,j)
    global t
    t = t + 1
    T[i-1] = t

def DFS_two(G,i):
    explored.update({i:True})
    for j in G[i-1][1::]:
        if explored[j]==False:
            DFS_two(G,j)
    print ("s2 = ",s)
    S.append(s)


def DFS_loop(G):
    i = len(G)
    global explored
    global T 
    while i>1:
        if explored[i]==False:
            DFS(G,i) 
        i = i-1 
    return T 

def DFS_loop_two(G,B=[]):
    global explored
    explored = {i+1:False for i in range(x)}
    global S 
    S = []
    for i in B:
        if explored[i]==False:
            global s 
            s = i
            print ("s=",s)
            DFS_two(G,s) 
    return S 

def sortout_T(A):
    scores = np.argsort(A)[::-1]
    scores = [i+1 for i in scores]
    return scores 

def main():

    G_list = list_from_txt('ENTER FILE ADDRESS')
    G_list_trans = invert_list_in_list(G_list)
    G_trans = edge_list_to_vertex(G_list_trans)
    G_regular = edge_list_to_vertex(G_list)
    Z = DFS_loop(G_trans)
    print ("first run complete!")
    Z = [i for i in Z]
    i = len(Z)
    print(i)
    P = sortout_T(Z)
    print ("descending order done!")
    jawab = DFS_loop_two (G_regular,P)
    jawab = [i for i in jawab]
    print ("jawab computed")
    print(most_frequent(jawab))

main()
