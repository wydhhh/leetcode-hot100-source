# 找到字符串中所有字母异位词
from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Counter() 相当于字典
        cnt_p = Counter(p)  # 统计 p 的每种字母的出现次数
        cnt_s = Counter()  # 统计 s 的定长子串t(窗口内)的每种字母的出现次数
        ans = []
        for right, c in enumerate(s):
            cnt_s[c] += 1             # 右端点进入窗口
            left = right - len(p) + 1 # 此时窗口左端点
            if left < 0:              # 窗口长度不足 len(p)
                continue
            if cnt_s == cnt_p:  # t(len_p) 和 p 的每种字母的出现次数都相同
                ans.append(left)  # 记录 t 的下标作为答案

            cnt_s[s[left]] -= 1  # 左端点离开窗口

        return ans

if __name__ == "__main__":
    # s = input()
    # p = input()
    s, p = input().split() # 实现空格分隔输入两串
    sol = Solution()
    res = sol.findAnagrams(s, p)
    
    print(' '.join(map(str, res)))