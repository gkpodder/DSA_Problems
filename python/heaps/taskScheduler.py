from typing import List
from collections import Counter, deque
from heapq import heapify, heappop, heappush


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapify(heap)
        q = deque()
        time = 0

        while heap or q:
            time += 1

            if heap:
                cnt = 1+heappop(heap)
                if cnt < 0:
                    q.append([cnt, time+n])

            if q and q[0][1] == time:
                heappush(heap, q.popleft()[0])

        return time
