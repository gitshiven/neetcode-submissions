class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer_set = set() # Duplicates ko filter karne ke liye set banaya
        
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                
                if total_sum == 0:
                    # Match mila toh tuple bana kar set mein daal do
                    answer_set.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif total_sum < 0:
                    j += 1
                else:
                    k -= 1
                    
        # Aakhiri mein set ko wapas list of lists mein convert kardo
        return [list(triplet) for triplet in answer_set]
