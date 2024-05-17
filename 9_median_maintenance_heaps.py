import heapq as heap

h_low = []
h_high = []
heap.heapify(h_low)
heap.heapify(h_high)
medians = []

with open('ENTER FILE NAME','r') as file:
    median_count = 10000000000
    for line in file:
        line = int(line)
        print(line)
        print(median_count)

        if line <= median_count:
            heap.heappush(h_low,-1*line)
            
        if line > median_count:
            heap.heappush(h_high,line)
        
        if len(h_low) - len(h_high) == 1:
            median_count = -1*h_low[0]
        
        if len(h_high) - len(h_low) == 1: 
            median_count = h_high[0]

        if len(h_low) - len(h_high) == 2:
            heap.heappush(h_high,-1*heap.heappop(h_low))
            
        if len(h_high) - len(h_low) == 2: 
            heap.heappush(h_low,-1*heap.heappop(h_high))
        
        if len(h_high) == len(h_low):
            median_count = -1*heap.nsmallest(1,h_low)[0]

        medians.append(median_count)

print(medians)

sum_medians = 0

for elements in medians:
    sum_medians = sum_medians + elements

print(sum_medians%10000)
