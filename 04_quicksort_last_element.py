import math 

def quick_sort_last_element(A):
    #base case - if n==1 or n==0
    if len(A) == 0:
        return A,0
    counter = len(A) - 1
    if len(A) == 1:
        return A,0 

    A[len(A)-1],A[0] = A[0],A[len(A)-1] #swapping the pivot i.e. the last element with the first 
    
    i = 1  #to keep track of the elements less than pivot so we can swap the pivot in at the end! 
    for j in range(1,len(A)):
        if A[j] > A[0]:
            continue
        if A[j] < A[0]:
            A[i],A[j] = A[j],A[i] #swap! This works even if i=j 
            i = i+1 #progress i so that elements with index less than i are all less than the pivot!
    #now time to swap the pivot into its rightful position 
    A[0],A[i-1] = A[i-1],A[0]
  
    if i==len(A): #taking care of edge case where the last element is the pivot 
        right = []
        left = A[0:i-1]
    elif i==1: #taking care of the edge case where the first element is the pivot 
        left = []
        right = A[i::]
    else:
        left = A[0:i-1]
        right = A[i::]

    left_sorted_array,left_counter = quick_sort_last_element(left) #solving left by recursion
    right_sorted_array, right_counter = quick_sort_last_element(right) #solving right by recursion
    A = left_sorted_array + [A[i-1]] + right_sorted_array #stiching the array back together
    return A , counter + left_counter + right_counter

question_array = []
with open ('INSERT FILE NAME','r') as file:
    for row in file: 
        question_array.append(int(row))

print (len(question_array))
a,b = quick_sort_last_element(question_array)
print (a[0],a[3212])
print (b)
