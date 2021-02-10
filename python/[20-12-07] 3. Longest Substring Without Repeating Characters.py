"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1 : return len(s)
        max_len = 0
        start = 0
        end = 1
        visited = {s[0]: 0}
        while end<len(s):
            if s[end] in visited and visited[s[end]]>=start:
                max_len = max(max_len, end - start)
                start = visited[s[end]] + 1
            visited[s[end]] = end
            end += 1
        return max(max_len, end - start)
