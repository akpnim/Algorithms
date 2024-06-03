#jobs given as weight,length in txt file 
#Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length)
#Tiebreak with jobs with higher weight first 

import numpy

def custom_sort(A):
    A_weights = [element[0] for element in A]
    index_by_weight = [element for element in numpy.argsort(A_weights)][::-1]
    A_weights = [A[i] for i in index_by_weight]
    return A_weights


A = []
with open('ENTER FILE NAME','r') as file: 
    for line in file:
        int_line = [int(i) for i in line.split()]
        A.append(int_line)

A = A[1::]

#A = [[5,3],[3,2],[4,2],[0,0]]

diff_A = [element[0]-element[1] for element in A] #creating an array of weight minus length

index_by_diff = [element for element in numpy.argsort(diff_A)][::-1] #getting indices for decreasing order of weight-length

A = [A[i] for i in index_by_diff] #arranging elements of A by decreasing order of indices of weight-length 


diff = A[0][0]-A[0][1]
i = 0 
temp =[]
ans = []

while i<len(A):
    if A[i][0] - A[i][1] == diff: 
        temp.append(A[i])
    if A[i][0] - A[i][1] != diff or i==len(A)-1: 
        add_to_ans = custom_sort(temp)
        for element in add_to_ans:
            ans.append(element)
        diff = A[i][0] - A[i][1]
        temp = []
        temp.append(A[i])
    i = i+1 

#now that we have our sorted A in ans, it is time to get the aggregate lengths for the sum computation

agg_l = []
running_agg = 0

for elements in ans: 
    running_agg = running_agg + elements[1]
    agg_l.append(running_agg)

weights_only = [element[0] for element in ans]

final_ans = numpy.dot(weights_only,agg_l)

print(final_ans)






