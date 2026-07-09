class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        l = 0
        r = l + 1
        
        while l < len(temperatures) - 1:
            if temperatures[r] > temperatures[l]:
                result[l] = r - l
                l += 1
                r = l + 1
            else:
                r += 1
                if r >= len(temperatures):
                    l += 1
                    r = l + 1
        
        return result