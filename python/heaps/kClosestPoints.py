from heapq import heapify, heappop
from typing import List
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        res = []

        for i in points:
            dist = math.sqrt(i[0]**2+i[1]**2)
            dists.append([dist, i[0], i[1]])
        heapify(dists)

        while k != 0:
            dist, x, y = heappop(dists)
            res.append([x, y])
            k -= 1
        return res
