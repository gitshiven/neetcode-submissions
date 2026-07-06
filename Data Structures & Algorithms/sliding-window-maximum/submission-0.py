
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        for i in range(len(nums)-k+1):     #kaunse index tak jayega, uske hisaab se loop banta hai
            window = nums[i:i+k]
            res.append(max(window))
        return res
                                                                                                       



