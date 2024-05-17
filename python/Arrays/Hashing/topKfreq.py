from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        count = [[] for i in range(len(nums)+1)]

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        for i in hashmap.keys():
            count[hashmap[i]].append(i)

        res = []
        for i in range(len(count) - 1, 0, -1):
            for i in count[i]:
                res.append(i)
            if len(res) == k:
                return res
