class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])

        answer = [intervals[0]]

        for start , end in intervals[1:]:
            if start <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1],end)
            else:
                answer.append([start,end])
        return answer