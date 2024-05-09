import math 
import random

def random_contraction_mincut(A):
    #while there are more than two vertices (n>2)
    while len(A)>2:
    #pick a remaining edge (u,v) uniformly at random
        vertex = random.choice(A)
        u,v = vertex[0],random.choice(vertex[1::])

    #find array starting with vertex v 
        v_index = 0
        u_index = 0
        for i in range(len(A)):
            if A[i][0]==v:
                v_index = i
            if A[i][0]==u:
                u_index = i

    #contract (u,v) into a single vertex 
        A[u_index] = A[u_index] + A[v_index]
        
    #removing vertex v altogether since it is merged above     
        A.pop(v_index)
    #replace all v with u in all arrays and removing self loops!
        for arrays in A:
            while v in arrays: 
                arrays[arrays.index(v)] = u
            while arrays[0] in arrays[1::]:
                arrays.pop(arrays[1::].index(arrays[0])+1)

    #returning cut represented by final two vertices 
    print(A)
    return len(A[0]) - 1 


C = []
with open (''ENTER FILE NAME'','r') as file: 
    for line in file: 
        D = []
        D = line.split()
        E =[]
        for i in range(len(D)):
            E.append(int(D[i]))
        C.append(E)
N = len(C)
print(N)

repititions = 1 #int(N*N*math.log(N)) #for large N this is good because probability of wrong answer is 1/N 
ans =[]
i = 0 
while i<repititions:
    ans.append(random_contraction_mincut(C))
    i = i+1

print (min(ans))