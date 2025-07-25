import heapq

def solution(scoville, K):
    count = 0
    heap = []
    
    # enque
    for s in scoville:
        heapq.heappush(heap, s)
        
    # mix
    while True:
        least_min = heapq.heappop(heap)
        if least_min >= K:
            break
            
        if len(heap) < 1:
            return -1
        
        next_min = heapq.heappop(heap)
        
        new_scoville = least_min + next_min * 2
        heapq.heappush(heap, new_scoville)
        count += 1
    
    return count