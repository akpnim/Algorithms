import math

def find_pivot(A):
    #finding the three elements to compare 
    first = A[0]
    last = A[len(A)-1]
    if len(A)%2 == 0:
        center = A[len(A)//2-1]
    else:
        center = A[len(A)//2]

    #picking the median 
    if (first<=center and center <= last) or (last<=center and center <= first) :
        pivot_index = A.index(center)
    elif (first<=last and last <= center) or (center<=last and last <= first) :
        pivot_index = A.index(last)
    elif (center <=first and first <= last) or (last <= first and first <= center) :
        pivot_index = A.index(first)
    
    return pivot_index



def quick_sort_medianofthree(A):
    #base case - if n==1 or n==0
    if len(A) == 0:
        return A,0
    
    counter = len(A) - 1

    if len(A) == 1:
        return A, counter
    
    if len(A) == 2:
        if A[0]>A[1]:
            A[0],A[1] = A[1],A[0]
            return A, counter
        else:
            return A, counter
    

    pivot_index = find_pivot(A)

    #swapping the pivot with the first element 

    A[pivot_index],A[0] = A[0],A[pivot_index]
    
    i = 1  #to keep track of the elements less than pivot so we can swap the pivot in at the end! 
    for j in range(1,len(A)):
        if A[j] > A[0]:
            continue
        if A[j] < A[0]:
            A[i],A[j] = A[j],A[i] #swap! This works even if i=j 
            i = i+1 #progress i so that elements with index less than i are all less than the pivot!
    #now time to swap the pivot into its rightful position 
    A[0],A[i-1] = A[i-1],A[0]
  
    if i==len(A):
        right = []
        left = A[0:i-1]
    elif i==1:
        left = []
        right = A[i::]
    else:
        left = A[0:i-1]
        right = A[i::]

    left_sorted_array,left_counter = quick_sort_medianofthree(left) #solving left by recursion
    right_sorted_array, right_counter = quick_sort_medianofthree(right) #solving right by recursion
    A = left_sorted_array + [A[i-1]] + right_sorted_array #stiching the array back together
    return A , counter + left_counter + right_counter

question_array = []
with open ('INSERT FILE NAME','r') as file:
    for row in file: 
        question_array.append(int(row))

print (len(question_array))
a,b = quick_sort_medianofthree(question_array)
print (a[0],a[3212],a[9999])
print(a)
print (b)

c = find_pivot([1,2,3,5,8,6,7])
print(c)

