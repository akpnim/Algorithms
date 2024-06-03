#jobs given as weight,length in txt file 
#Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the ratio weight/length
#Tiebreak with jobs with same ratio is arbitrary! 

import numpy



A = []
with open('ENTER FILE NAME','r') as file: 
    for line in file:
        int_line = [int(i) for i in line.split()]
        A.append(int_line)

A = A[1::]

#A = [[5,3],[3,2],[4,2],[0,0]]

ratio_A = [element[0]/element[1] for element in A] #creating an array of only ratios

index_by_ratio = [element for element in numpy.argsort(ratio_A)][::-1] #getting indices for decreasing order of the ratio

A = [A[i] for i in index_by_ratio] #arranging elements of A by decreasing order of indices of ratio


#now that we have our A above, it is time to get the aggregate lengths for the sum computation

agg_l = []
running_agg = 0

for elements in A: 
    running_agg = running_agg + elements[1]
    agg_l.append(running_agg)

weights_only = [element[0] for element in A]

final_ans = numpy.dot(weights_only,agg_l)

print(final_ans)






