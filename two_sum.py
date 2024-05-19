counter = 0 
A =[]
with open('ENTER FILE LOCATION','r') as file:
    for line in file: 
        A.append(int(line))
        counter = counter + 1 

A = sorted(A)

i = 0 
j = len(A) - 1 
sums = set()

while i != j: 
    if A[i] + A[j] < -10000:
        i = i+1
        continue  
    if A[i] + A[j] > 10000:
        j = j-1 
        continue 
    if A[i] != A[j]:
        sums.add(A[i] + A[j])
    i = i+1 
print(len(sums))
