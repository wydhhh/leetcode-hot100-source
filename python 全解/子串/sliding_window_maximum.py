# 滑动窗口最大值浏览
from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])
        
        return ans
    
if __name__ == "__main__":
    data = list(map(int, input().split()))
    nums = data[:-1]
    k = data[-1]
    
    sol = Solution()
    ans_list = sol.maxSlidingWindow(nums, k)
    print(' '.join(map(str, ans_list)))