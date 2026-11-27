class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free = list(range(n))
        busy = []

        count = [0] * n

        for start,end in meetings:
            while busy and busy[0][0]<= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(free,room)
            if free:
                room = heapq.heappop(free)
                heapq.heappush(busy, (end, room))
            else:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(busy,(end_time + (end - start), room))
            count[room] += 1
        
        return count.index(max(count))
