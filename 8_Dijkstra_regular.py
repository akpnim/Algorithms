"""task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, and to compute
 the shortest-path distances between 1 and every other vertex of the graph. If there is no path between a vertex 
 v and vertex 1, we'll define the shortest-path distance between 1 and 
v to be 1000000. """
import numpy as np
#Step 1 is to covert the raw data in the text file into an array of vertices V 
V = []
with open('ENTER FILE NAME','r') as file:
    for line in file: 
        a = line.split('\t')
        a.pop()
        for element in a:
            a[a.index(element)] = element.split(',')
        for (i,j) in enumerate(a):
            for itemss in j:
                j[j.index(itemss)] = int(itemss)
        a[0] = a[0][0]
        V.append(a)

#Step 2 is to initialize the key strucutres
s = 1 #source vertex is 1 
X = [s] #Vertices processed so far 
X_bool = [False]*len(V)
X_bool[s-1] = True
A = [1000000]*len(V) #Computed shortest path distances for corresponding ith vertex in X 
A[s-1] = 0 
B = ['']*len(V) #Computed shortest path (optional) 
B[s-1] =''

#Step 3 is to execute the loop 
while X_bool != [True]*len(V): 
    distances = []
    vertices = []
    for nodes in X:
        for i,j in enumerate(V[nodes-1][1::]):
            if j[0] not in X:
                distances.append(j[1]+A[nodes-1])
                vertices.append(j[0])
    mini = 1000000
    min_index = 0

    for (i,j) in enumerate (distances):
        if j <= mini: 
            mini = j
            min_index = i
    X.append(vertices[min_index])
    X_bool[vertices[min_index]-1] = True
    A[vertices[min_index]-1] = mini 
    B[vertices[min_index]-1] = B[s-1] + str(vertices[min_index])
    s = vertices[min_index]

Question = [7,37,59,82,99,115,133,165,188,197]
Answer = []
for vertex in Question:
    Answer.append(A[vertex-1])
print (Answer)


                

