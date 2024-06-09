#First step is to run Bellman ford algorithm in O(mn) time to check for negative cycles 
#Second step is to run the bellman ford algorithm in O(mn) * n times = O(mn^2) for the small graph case
#for large or a dense graph it makes more sense to run Johnson's algorithm that runs in nmlog(n) time vs mn^2 
#g1 has a negative cycle 
#g2 has a negative cycle 
#g3 has no negative cycle!!!

import math 
import time 
import heapq

Graph = [] 
with open(ENTER FILE NAME,'r') as file: 
    for line in file: 
        Graph.append([int(i) for i in line.split()])


n = Graph[0][0]

Graph = Graph[1::]

in_vertices = {}  # {1:[[2,10],[3,11]]} would mean vertex 1 has incoming vertices 2 and 3 with weights 10 and 11 

for edge in Graph: #we care about the in-deg vertices of each vertex so let's create in_vertices from the Graph 
    if edge[1] in in_vertices:
        in_vertices[edge[1]].append([edge[0],edge[2]])
    else: 
        in_vertices[edge[1]] = [[edge[0],edge[2]]]

#running bellman ford to check if the graph has cycles - let source vertex be 1 



def bellman_ford(incoming_vertices: dict) -> dict:
    A = {}
    for v in range(1,n+1): #set all distances as infinity...
        A[(0,v)] = math.inf
    
    A[(0,1)] = 0 #...except for the distance from source to itself 

    for i in range(1,n+1):
        stable = True 
        for v in range(1,n+1):
            candidates = [A[(i-1,v)]]
            for inward_edge in in_vertices[v]:
                candidates.append(A[(i-1,inward_edge[0])] + inward_edge[1])
            A[(i,v)] = min(candidates)
            if A[(i,v)] != A[(i-1,v)]:
                stable = False 
        if stable == True: 
            min_distances = {}
            for v in range(1,n+1):
                min_distances[v] = A[(i-1,v)]
            return min_distances
    return {"negative cycle"}

bellman_ford(in_vertices)

def all_pairs_shortest_path(incoming_vertices: dict) -> dict:
    A = {}
    min_distances = []
    for s in range(1,n+1):
        print(s)
        for v in range(1,n+1): #set all distances as infinity...
            A[(0,v)] = math.inf
        A[(0,s)] = 0 #...except for the distance from source to itself 
        for i in range(1,n+1):
            stable = True 
            for v in range(1,n+1):
                candidates = [A[(i-1,v)]]
                for inward_edge in in_vertices[v]:
                    candidates.append(A[(i-1,inward_edge[0])] + inward_edge[1])
                A[(i,v)] = min(candidates)
                if A[(i,v)] != A[(i-1,v)]:
                    stable = False 
            if stable == True: 
                distances = [] 
                for v in range(1,n+1):
                    distances.append(A[(i-1,v)])
                min_distances.append(min(distances))
                break 
        
    return min(min_distances)

print(all_pairs_shortest_path(in_vertices))
