class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_heap=[] #min heap to find least capital

        for i in range(len(capital)):
            heapq.heappush(min_heap,(capital[i],profits[i]))
        
        available=[] #max heap to find max profit

        for _ in range(k):
            while min_heap and min_heap[0][0]<=w:
                cap,profit=heapq.heappop(min_heap)
                heapq.heappush(available, -profit)
            
            if not available:
                break
            
            maxprofit=-heapq.heappop(available)
            w+=maxprofit
        return w
            

        
