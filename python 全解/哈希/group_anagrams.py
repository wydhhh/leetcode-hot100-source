# 字母异位词分组
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)  
        for s in strs:
            sorted_s = ''.join(sorted(s))  
            d[sorted_s].append(s)  
        return list(d.values())

if __name__ == "__main__":
    line = input().strip() # 去掉开头结尾的空白字符，有没有都行
    strs = line.split(",")

    sol = Solution()
    result = sol.groupAnagrams(strs)

    for group in result:
        print(",".join(group))