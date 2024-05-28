#What is the maximum spacing of a 4-clustering? - Single link clustering
#initially each point in a separate cluster 
#repeat until only k clusters 
#let p,q be closest pair of separated points 
#merge clusters with p and q into a single cluster (iff no cycles formed i.e. find(p)!= fine(q)) - using union-find data structure

import time 

import numpy

start = time.time()
#Python doesn't have a default disjoint set or unionfind so creating one -  

class UnionFind:
    def __init__(self,n):
        self.parent = [i+1 for i in range(n)] #initialzing all the parents as self
        self.rank = [1 for i in range(n)] #initializing all the ranks as 1 
        self.count = n

    def find(self,p):
            if self.parent[p-1] != p:
                self.parent[p-1] = self.find(self.parent[p-1]) #recursively sets all the parents on the entire path to the root (path compression)
            return self.parent[p-1]
    
    def union(self,p,q):
        root_p = self.find(p)
        root_q = self.find(q)
        if self.rank[p-1] == self.rank[q-1]:
            self.parent[root_p-1] = root_q
            self.rank[root_q-1] = self.rank[root_q-1] + 1 
        if self.rank[p-1] > self.rank[q-1]:
            self.parent[root_q-1] = root_p
        if self.rank[p-1] < self.rank[q-1]:
            self.parent[root_p-1] = root_q
        self.count = self.count - 1 
        


A=[]
with open ('ENTER FILE NAME','r') as file: 
    for line in file: 
        a = [int(i) for i in line.split()]
        A.append(a)
A = A[1::]

#let's sort A in increasing order of costs 
edges_only = [edge[2] for edge in A]
edges_indices = [i for i in numpy.argsort(edges_only)]
A = [A[i] for i in edges_indices]
T = UnionFind(500)

ans = []

for edge in A:
    p = edge[0]
    q = edge[1]
    if T.find(p) != T.find(q):
        T.union(p,q)
    if T.count == 3: #basically the max spacing 4-clustering is the edge length for the edge that would decrease the no of clusters to 3 
        print (edge)
        break 
    
stop = time.time()

print(stop-start,'s')
