class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)
        minHeap = []
        
        for interval in intervals:
            if minHeap and minHeap[0 ]<= interval.start:
                heapq.heappop(minHeap)
            
            heapq.heappush(minHeap,interval.end)

        return len(minHeap)

        
