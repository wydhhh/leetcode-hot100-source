# 最长连续序列
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        m = len(st)
        ans = 0
        for x in st:
            if x - 1 in st:  # 如果 x 不是序列的起点
                continue
            # x 确认是序列的起点
            y = x + 1
            while y in st:  # 不断查找下一个数是否在哈希集合中
                y += 1
            ans = max(ans, y - x)  # 从 x 到 y-1 一共 y-x 个数
            if ans * 2 >= m:  # ans 不可能变得更大
                break
        return ans
    
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    
    sol = Solution()
    print(sol.longestConsecutive(nums))