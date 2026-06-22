class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        left = 0
        
        find_duplicate = set()

        for right in range(len(s)):
            while s[right] in find_duplicate:
                find_duplicate.remove(s[left])
                left+=1
            find_duplicate.add(s[right])
            max_count = max(max_count, right - left + 1)
        return max_count