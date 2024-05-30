

A = []
with open('ENTER FILE DESTINATION','r') as file:
    for line in file: 
        A.append(int(line))

Original = A[1::]
#Original = [3,6,1,2,4,1] - Test case 
A = [] 
A.append(0) #initializing the MWI array
A.append(Original[0]) #initializing the MWI array
i = 2 #initializing the counter for for loop 
while i < len(Original) + 1: #for the recursion to work we need to have A[0] = 0 as an 'extra' element, thus making A one item longer
    A.append(max(A[i-1],A[i-2]+Original[i-1])) 
    i+= 1 

#now time for reconstrucition
i = len(A) -1 #initializing counter
recon = set() #set of vertices that are included in A 
while i > 0: 
    if A[i-1] >= A[i-2] + Original[i-1]:
        i = i -1 
    else: 
        recon.add(i)
        i = i -2 

question_list = [1, 2, 3, 4, 17, 117, 517, 997]
answer_string = ""
for element in question_list: 
    if element in recon: 
        answer_string += '1'
    else: 
        answer_string += '0'

print(answer_string)
