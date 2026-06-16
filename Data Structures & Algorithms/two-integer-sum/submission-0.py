class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap_ka_koi_bhi_naam_rakhlo = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashmap_ka_koi_bhi_naam_rakhlo:
                return [hashmap_ka_koi_bhi_naam_rakhlo[diff], i]
            hashmap_ka_koi_bhi_naam_rakhlo[n] = i
        return
                    