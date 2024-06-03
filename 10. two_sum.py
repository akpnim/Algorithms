#The solution below is more straightforward than using hash tables! Sometimes it is not necessary to use more complex data structures when the solution is simple. 
#The goal is to find the number of distict tagets T in the inclusive range [-10000,10000] for the sum of x,y for distinct integers in A. 

A =[]
with open('ENTER FILE NAME','r') as file:
    for line in file: 
        A.append(int(line))

A = sorted(A)

upper = 10000
lower = -10000
sums = set()

i = 0 
j = len(A) - 1 
while i != j: 
    if A[i] + A[j] > upper:
        j = j-1
        continue
          
    if A[i] + A[j] < lower:
        i = i+1
        continue

    if abs(upper - A[i] - A[j]) > abs(lower - A[i] - A[j]): #if the sum is on the "left" side, traverse i over to the right
        while A[i] + A[j] < upper and A[i] + A[j] > lower and i !=j: 
            if A[i]!=A[j]:
                sums.add(A[i]+A[j])
            i = i+1
         
    if abs(upper - A[i] - A[j]) < abs(lower - A[i]-A[j]): #if the sum is on the "right" side, traverse j over to the left
        while A[i] + A[j] > lower and A[i] + A[j] < upper and i !=j:
            if A[i] != A[j]:
                sums.add(A[i]+A[j])
            j = j-1
            
print(len(sums))
