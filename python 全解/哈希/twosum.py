# 两数之和
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()
        for idx, val in enumerate(nums):
            if target - val not in records:
                records[val] = idx
            else:
                return [records[target - val], idx]
        return []

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    target = int(input())
    
    sol = Solution()
    res = sol.twoSum(nums, target)
    
    if res:
        print(" ".join(map(str, res)))
    else:
        print("none")