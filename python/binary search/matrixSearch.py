from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row, col = len(matrix), len(matrix[0])

        if matrix[-1][-1] < target or matrix[0][0] > target:
            return False

        bot, top = 0, row - 1

        while bot <= top:
            row = (top + bot) // 2
            if matrix[row][-1] < target:

                bot = row + 1
            elif matrix[row][0] > target:

                top = row - 1
            else:
                break

        if bot > top:
            return False

        row = (bot + top) // 2
        l, r = 0, col - 1
        while l <= r:
            mid = (l+r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
        return False
