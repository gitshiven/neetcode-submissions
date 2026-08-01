class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. Merge ke baad sort karna zaroori hai
        merged = sorted(nums1 + nums2)                 # O(Nlogn add hogya)
        
        # 2. Total length ke hisab se mid index nikalna
        l,r = 0, len(merged)-1
        mid = (l+r)/2  # Yeh float bhi ho sakta hai (e.g., 1.5)

        if not mid.is_integer():
            l = math.ceil(mid)
            r = math.floor(mid)
            median = (merged[l]+merged[r])/2
            return median
        else:
            return merged[int(mid)]
    
        
            
 