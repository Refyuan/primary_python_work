# 给定一个字符串s ，请你找出其中不含有重复字符的最长子串的长度。
# s由英文字母、数字、符号和空格组成。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        str_set={}
        left=0
        for i in range(len(s)):
            if s[i] in str_set:
                left=max(left,str_set[s[i]])
            str_set[s[i]] = i
            res=max(res,i-left)
        return res
if __name__ == '__main__':
    s = Solution()

    print(s.lengthOfLongestSubstring("abcabcbb"))