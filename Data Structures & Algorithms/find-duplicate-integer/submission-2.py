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
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow  
        
        
