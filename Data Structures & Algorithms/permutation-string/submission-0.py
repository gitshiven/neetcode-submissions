#O(n)  
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        counts1 = {}
        counts2 = {}
        left = 0
        for count in s1:
            counts1[count] = 1+counts1.get(count,0)
        for right in range(len(s2)):
            counts2[s2[right]] = 1 + counts2.get(s2[right],0)
            while(right-left+1)>window_size:
                counts2[s2[left]]-=1
                if counts2[s2[left]] == 0:
                    del counts2[s2[left]]
                left+=1
            if counts1 == counts2:
                return True
        return False    
                



            
            

