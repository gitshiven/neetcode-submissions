#O(log n)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = max(nums)
        l,r = 0, len(nums)-1

        while l <=r:
            mid = (l+r)//2
            k = nums[mid]
            res = min(k, res)

            if k>nums[r]:
                l = mid+1
            else:
                r = mid-1
        return res


            
          