
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

def switch_bit(a):
    if a=='1':
        return '0'
    if a=='0':
        return '1'
    else:
        return "error!"

def complement_set(A):
    C = set()
    i = 0 
    h1s = ""
    element = A
    C.add(A)
    while i<len(element):
        h1s = element[0:i] + switch_bit(element[i]) + element[i+1::]
        C.add(h1s)
        j = i+1 
        h2s = ""
        while j<len(h1s):
            h2s = h1s[0:j] + switch_bit(element[j]) + element[j+1::]
            C.add(h2s)
            j+=1 
        i += 1 
    return C 

A = []
with open('ENTER FILE NAME','r') as file: 
    for line in file: 
        A.append(line.strip().replace(" ",""))
A = A[1::]

print("done")

print("initializing unionfind operations...")

T = UnionFind(len(A))
print("creating masters dictionary")
master = {}
for (ind,element) in enumerate(A):
    if element in master: #way to handle duplicate vertices with the same bitstring
        master[element].append(ind+1)
    elif element not in master:
        master[element] = [ind+1]
print("done creating master dictionary")
print(len(master))

m = 0 

while m < len(A):
    comple_set = complement_set(A[m])
    for element in comple_set: 
        if element in master: 
            for vertex in master[element]:
                if T.find(m+1) != T.find(vertex):
                    T.union(m+1,vertex)
    m+=1

print("Number of clusters in case where no two vertices with hamming \n distance less than 3 are in different clusters:")

print(T.count)






