#O(n)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countT={}
        window={}

        res = [-1,-1] 
        reslen = float("infinity")

        for c in t:
            countT[c] = 1 + countT.get(c,0)   #counting individiual character's values
        
        have = 0
        need=len(countT)
        l=0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)  #counting values that we find in window along the iteration
            

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have+=1 
            
            while have == need:
                if(r-l+1)<reslen:
                    res = [l,r]
                    reslen = (r-l+1)

                window[s[l]]-=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if reslen!= float("infinity") else ""  #value_if_true if condition else value_if_false



                



