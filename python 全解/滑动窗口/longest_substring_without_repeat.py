# 无重复字符的最长子串
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i) # 更新左指针，指向该字符最后索引
            dic[s[j]] = j # 哈希表更新：该字符最后出现的索引
            res = max(res, j - i) # 更新答案
        return res
    
if __name__ == "__main__":
    
    input_str = input()
    sol = Solution()
    result = sol.lengthOfLongestSubstring(input_str)
    print(result)