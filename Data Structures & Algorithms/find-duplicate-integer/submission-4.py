class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Floyd's Cycle Detection
        slow = fast = nums[0]
        #Cycle dhundo
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow_2 = nums[0]
        while True:
            if slow==slow_2:
                break
            slow_2 = nums[slow_2]
            slow = nums[slow]
    
        return slow  
        
        
