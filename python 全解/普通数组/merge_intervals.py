# region 初始化合并
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda p: p[0])  # 按照左端点从小到大原地排序
                                            # p: p[0] 是从元素到排序依据的映射 lambda 函数
        ans = []
        for p in intervals:
            if ans and p[0] <= ans[-1][1]:  # 新区间可以合并（接壤/重叠）
                ans[-1][1] = max(ans[-1][1], p[1])  # 更新右端点
            else:  # 不相交，无法合并
                ans.append(p)  # 新的独立区间
        return ans

# 第一版 main
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    intervals = []
    for i in range(0, len(nums), 2):
        L = nums[i]
        R = nums[i+1]
        intervals.append([L, R])
    
    sol = Solution()
    res = sol.merge(intervals)
    
    for L, R in res:
        print(L, R)
        
# 第二版 main
if __name__ == "__main__":
    # 第一步：输入个数 N
    n = int(input())
    intervals = []
    
    # 第二步：输入 N 行，每行两个数
    for _ in range(n):
        L, R = map(int, input().split())
        intervals.append([L, R])
    
    sol = Solution()
    res = sol.merge(intervals)
    
    # 输出：每一行一个区间
    for L, R in res:
        print(L, R)
        
# 第三版 main (依赖于空行结束)
if __name__ == "__main__":
    intervals = []

    while True:
        line = input().strip()
        if not line:
            break
        a, b = map(int, line.split())
        intervals.append([a, b])

    sol = Solution()
    res = sol.merge(intervals)
    for a, b in res:
        print(a, b)