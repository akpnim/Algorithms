import time 
a = time.time()
G = []
with open('ENTER FILE NAME','r') as file: 
    for line in file: 
        G.append([int(i) for i in line.split()]) # v = G[i][0] value and w = G[i][1] weight starting from i=1 

W = G[0][0] #size

n = G[0][1] #number 

A = [[] for j in range(n+1)] #2-D array intialization in linear time

print(len(A))

#initialization step A[0,x] = 0 for all x since value is 0 for the null set 
for i in range(W+1):
    A[0].append(0)

for i in range(1,n+1):
    for x in range(W+1):
        if G[i][1] > x:
            A[i].append(A[i-1][x])
        else: 
            A[i].append(max(A[i-1][x] , A[i-1][x-G[i][1]] + G[i][0]))
    print(i)

print(A[n][W])
b = time.time()
print(b-a,'s')
