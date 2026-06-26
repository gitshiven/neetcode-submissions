class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left<=right:
            middle = (left+right)//2
            if target == nums[middle]:
                return middle

            if nums[left]<=nums[middle]:            # ye check karra hu mai to see kaunsi side sorted hai; Left ya right
                if target > nums[middle] or target < nums[left]: #isme se agar ek bhi false hojata toh matlab value left portion mai hi hai and agar True hote dono toh matlab value left ki range se bahar hai, right mai check karo
                    left = middle + 1
                else:
                    right = middle - 1

            else:                      #right sorted portion
                if target > nums[right] or target < nums[middle]:
                    right = middle -1
                else:
                    left = middle + 1
        return -1
                


