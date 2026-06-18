class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range(1, len(nums)):
            left.append(left[i-1] * nums[i-1])

        right = [1] * len(nums)   # isme empty isliye nahi banayi kyuki isme right se value insert karni hai and append sirf left to right work karta hai. isliye pehle index ke saath banayi list(array)
        for i in range(len(nums)-2, -1, -1):  # *len(nums) matlab ye value itni baar repeat karo i.e. len(nums)
            right[i] = right[i+1] * nums[i+1]

        output = []     #output = [0] * len(nums)  aise bhi kar sakte hai
        for i in range(len(nums)):
            output.append(left[i] * right[i]) #but fir yaha  output[i] = left[i] * right[i]

        return output