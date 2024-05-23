import numpy 
import timeit
import heapq

start = timeit.default_timer()

def xor(a,b):
    if a and b: 
        return False 
    if not a and not b: 
        return False
    if a and not b: 
        return True 
    if b and not a: 
        return True 

A = []
with open('ENTER FILE NAME','r') as file: 
    for line in file:
        int_line = [int(i) for i in line.split()]
        A.append(int_line)

A = A[1::]

X = [False]*500 
X[0] = True #intiializing X 
T = [] #initializing T 

while X != [True]*500: 
    temp = []
    temp_dict = {}
    for edge in A: 
        if xor(X[edge[0]-1],X[edge[1]-1]): 
            heapq.heappush(temp,edge[2])
            temp_dict[edge[2]] = edge
    min_key = temp[0]
    T.append(temp_dict[min_key])
    X[temp_dict[min_key][0]-1] = True
    X[temp_dict[min_key][1]-1] = True
    A.pop(A.index(temp_dict[min_key])) 

weights = [element[2] for element in T]

sum = 0 

for element in weights: 
    sum = sum + element 

print (sum)


stop = timeit.default_timer()

print('Time:', stop - start)  


