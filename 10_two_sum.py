#The solution below is more straightforward than using hash tables! Sometimes it is not necessary to use more complex data structures when the solution is simple. 
#The goal is to find the number of distict tagets T in the inclusive range [-10000,10000] for the sum of x,y for distinct integers in A. 

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
