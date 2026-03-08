# 和为 K 的子数组
from collections import defaultdict
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = s = 0
        for x in nums:
            cnt[s] += 1  # 不必单独记录 0 出现了 1 次
            s += x
            ans += cnt[s - k]
        return ans
    
if __name__ == "__main__":
    data = list(map(int, input().split()))
    nums = data[:-1]
    k = data[-1]
    
    sol = Solution()
    print(sol.subarraySum(nums, k))