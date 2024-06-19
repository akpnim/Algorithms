#This is the nearest neighbour heuristic implementation of the travelling salesman problem

#(1) Start the tour at the first city.

#(2) Repeatedly visit the closest city that the tour hasn't visited yet.  
# In case of a tie, go to the closest city with the lowest index.  
# For example, if both the third and fifth cities have the same distance from the first city 
# (and are closer than any other city), then the tour should begin by going from the first city to the third city.

#(3) Once every city has been visited exactly once, return to the first city to complete the tour.

import math
import time 
import numpy
import matplotlib.pyplot as plt

start = time.time()

cordinates = []
with open('','r') as file: 
    for line in file: 
        a = [float(i) for i in line.split()[1::]]
        if len(a)>1:
            cordinates.append((a[0],a[1]))

#cordinates = [(1,1),(2,3), (3,4), (4,6)] #TEST CASE! .. answer = 11.72
#TSP answer = 26442.73

n = len(cordinates)

def distances_generate(A: list) -> numpy.array: #list of tuples -> dict of v1v2 distances 
    distances = numpy.empty((n+1,n+1))
    for index1,coordinate1 in enumerate(A):
        for index2,coordinate2 in enumerate(A):
            distances[index1 + 1,index2 + 1] = ((coordinate1[0]-coordinate2[0])**2 + (coordinate1[1]-coordinate2[1])**2)
        print(index1)
    return distances

distances = distances_generate(cordinates)
visited = {0,1}
route = []
vertices = {i for i in range(n+1)}
total_distance = 0
current = 1

while visited != vertices:
    indices_sorted = [i for i in numpy.argsort(distances[current],kind="stable")]
    for i in indices_sorted:
        if i not in visited:
            total_distance = total_distance + numpy.power(distances[current][i],0.5)
            route.append([current,i])
            current = i 
            visited.add(current)
            break
    print(len(visited))
print(total_distance,current)
route.append([current,1])
total_distance = total_distance + numpy.power(distances[current][1],0.5)
print("total_distance = ", total_distance)
a = 0
for edge in route: 
    a += round(distances[edge[0]][edge[1]]**(1/2),4)
print("rounded_distance =", a)
#print(route) 
print(time.time() - start,'seconds to complete')
exit()

#let's visualize this 
path = []
for i,j in enumerate(route):
    if i==0:
        path.append(j[0])
        path.append(j[1])
    else:
        path.append(j[1])
print("tour length = ",len(path))


x_values = [cordinates[i-1][0] for i in path]
y_values = [cordinates[i-1][1] for i in path]
plt.scatter(x_values, y_values, color='blue', marker='X')
plt.plot(x_values, y_values, color='green', linestyle='--') #connects in order of x,y values 
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Visualisation of TSP-NN heuristic')

# Annotate points
for i, j in enumerate(path):
    plt.annotate(f'{j}', (cordinates[j-1][0], cordinates[j-1][1]))

# Show the plot with a grid
plt.grid(True)
plt.show()


