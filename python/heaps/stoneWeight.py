from heapq import heapify, heappop, heappush

from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)

        while len(stones) > 1:
            one = heappop(stones)
            two = heappop(stones)
            if one < two:
                heappush(stones, one-two)
        if stones:
            return stones[0]*-1
        else:
            return 0
