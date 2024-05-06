import math 

def invert_sort(A):
#defining base cases where length of array is 2
    answer = []
    n = len(A)
    if n == 1: 
        return A,0
    if n == 2: 
        if A[1] < A[0]:
            answer.append(A[1])
            answer.append(A[0])
            return answer,1
        else: 
            return A,0 

    if n > 2: 
        mid = n//2 
        B = A[:mid]
        C = A[mid:]
        #print (B)
        #print (C)
        B,count_addB = invert_sort(B)
        C,count_addC = invert_sort(C)
        #print (B)
        #print(C)
        #print (n)
        i = 0
        j = 0
        cross_count = 0
        for k in range(n):
            if j == len (C): #stop case
                answer = answer + B[i:]
                break

            if i == len(B): #stop case 
                answer = answer + C[j:]
                break

            if B[i] > C[j]:            
                answer.append(C[j])
                j = j+1 
                cross_count = cross_count + (len(B)-i)
                continue

            if B[i] < C[j]:
                answer.append(B[i])
                i = i+1
        total_count = count_addB + count_addC + cross_count
        #print ("cross_count = ", cross_count)
        #print ("total_count = ", total_count)
        return answer, total_count


question = []
with open ('/Users/adityapatel/Desktop/Back-end/stanford_algorithms/Course1/question_array.txt','r') as file:
    for line in file: 
        question.append(int(line)) #converting to int is important otherwise it will store as strings 

ans,count = invert_sort(question)

print (count)





