class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}

        left = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right],0)

            if((right-left+1) - max(count.values())) <=k :
                res = max(res, (right-left+1))
            else :
                count[s[left]]-=1
                left+=1
             
        return res

                                                









#max(count.values()) isse max value milti hai value ki out of all the values in hashmap