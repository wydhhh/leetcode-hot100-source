# 轮转数组
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(i: int, j: int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        k %= n  # 轮转 k 次等于轮转 k % n 次，这是周期性
        reverse(0, n - 1) # 整个数组倒置，目的是交换两个子数组的位置
        reverse(0, k - 1) # 恢复倒置前数组
        reverse(k, n - 1) # 恢复倒置后数组
        
if __name__ == "__main__":
    input_str = input()
    nums = list(map(int, input_str.split()))
    k = int(input())
    
    sol = Solution()
    sol.rotate(nums, k)
    
    print(' '.join(map(str, nums)))