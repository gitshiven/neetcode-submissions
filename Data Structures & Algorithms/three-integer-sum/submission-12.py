#O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i,a in enumerate(nums):
            if i>0 and nums[i-1] == a: 
                continue
            left,right = i+1,len(nums)-1

            while left<right:
                sum = nums[i] + nums[left] + nums[right]
                if sum>0:
                    right-=1
                elif sum < 0:
                    left+=1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left+=1

                    while (nums[left]==nums[left-1] and left<right):   #important line #come back to this again
                        left+=1
        return res 

            
            

                
                
    

            

        


        