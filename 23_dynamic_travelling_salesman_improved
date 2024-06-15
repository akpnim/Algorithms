#Optimized code that uses numpy array instead of regular array 
#also uses concurrent computing for running the main subroutine on subsets of same cardinality.

import math 
import itertools
import time 
import concurrent.futures
import numpy

start = time.time()

cordinates = []
with open('ENTER FILE NAME','r') as file: 
    for line in file: 
        a = [float(i) for i in line.split()]
        if len(a)>1:
            cordinates.append((a[0],a[1]))

#cordinates = [(1,1),(2,3),(3,4),(4,6)] #TEST CASE! .. answer = 11.68 
#n = 4
n = 25

def distances_generate(A: list) -> dict: #list of tuples -> dict of v1v2 distances 
    distances = {}
    for index1,coordinate1 in enumerate(A):
        for index2,coordinate2 in enumerate(A):
                distances[(index1 + 1,index2 + 1)] = math.sqrt((coordinate1[0]-coordinate2[0])**2 + (coordinate1[1]-coordinate2[1])**2)
    return distances

distances = distances_generate(cordinates)

vertices = [i for i in range(1,n+1)]

def subsets(A: list, m: int) -> list: #set A of vertices [1,2,3,...,n] -> subsets of size m containing 1
    answer = []
    for i in itertools.combinations(A[1::],m-1):
        B = list("1" + "".join("0" for _ in range(n-1)))
        for j in i: 
            B[j-1] = '1'
        answer.append("".join(str(i) for i in B))
    return answer

all_subsets = [subsets(vertices,m) for m in range(1,n+1)] #basically the ith array within all_subsets yields subsets with i vertices  

#all_subsets = list(itertools.starmap(subsets,zip(V,X)))

print(len(all_subsets),"done calculating and storing all the subset bitstrings for easy access!") 

print("initializing array...")

A = numpy.empty((2**(n-1),n)) #numpy array takes much less time to initialise 

#A = [[[] for i in range(n)] for _ in range(int("111111111111111111111111",2)+1)] # 2^(n-1)rows - this appraoch is super-slow 

print("done initializing array!")

for element in all_subsets[1]:
    for i,j in enumerate(element):
        if j=="1" and i!=0:
            A[int(element[1::],2)][i] = distances[(1,i+1)]
        if j=="1" and i==0:
            A[int(element[1::],2)][i] = 0

print("initialization complete!Entering main for loop-")

def main_loop(S: list):
    for i,j in enumerate(S):
            if j=="1" and i!=0: 
                jay = i+1
                S_minus_j = S[0:jay-1] + "0" + S[jay::]
                candidates = []
                for l,k in enumerate(S): 
                    if k=="1" and i!=l and l!=0:
                        kay = l+1
                        candidates.append(A[int(S_minus_j[1::],2)][kay-1] + distances[(kay,jay)])
                A[int(S[1::],2)][jay-1] = min(candidates)

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor: 
        for m in range(3,n+1):
            list(executor.map(main_loop, all_subsets[m-1]))
            print(m,time.time()-start)
    print("entering minimum computaitons...")
    ans = []
    for j in range(2,n+1):
        ans.append(A[int(all_subsets[n-1][0][1::],2)][j-1] + distances[(j,1)])
        print( j, A[int(all_subsets[n-1][0][1::],2)][j-1],  distances[(j,1)],  A[int(all_subsets[n-1][0][1::],2)][j-1] + distances[(j,1)])
    print(min(ans))

if __name__ == "__main__":
    main()

