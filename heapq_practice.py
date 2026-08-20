import heapq

heap = []   #using heapq to create a priority queue

#add elements to the heap with their priorities
heapq.heappush(heap, (3, "Andy"))    
heapq.heappush(heap, (1, "Bob"))   
heapq.heappush(heap, (7, "Carol"))   
heapq.heappush(heap, (2, "Sam"))   
heapq.heappush(heap, (5, "Lily"))    


while heap:
    priority, name = heapq.heappop(heap)   #pop elements from the heap based on their priority (lowest priority first)
    print(f"Priority: {priority}, Name: {name}")