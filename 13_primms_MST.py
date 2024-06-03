import numpy 
import time

start_time = time.time()

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

X = {1}
T = []

while len(X)!= 500: 
    temp = []
    for edge in A: 
        if xor(edge[0] in X,edge[1] in X): 
            temp.append(edge)
    weights = [element[2] for element in temp]
    index_by_weights = [i for i in numpy.argsort(weights)]
    min_index = index_by_weights[0]
    T.append(temp[min_index])
    X.add(temp[min_index][0])
    X.add(temp[min_index][1])

weights = [element[2] for element in T]

sum = 0 

for element in weights: 
    sum = sum + element 

print (sum)

    
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")


