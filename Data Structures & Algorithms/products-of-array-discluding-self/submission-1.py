class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        # Initialize arrays with 1s
        prefix = [1] * n
        suffix = [1] * n
        lst = [1] * n
        
        # Step 1: Fill the prefix array
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            
        # Step 2: Fill the suffix array
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
            
        # Step 3: Multiply prefix and suffix elements to get the final answer
        for i in range(n):
            lst[i] = prefix[i] * suffix[i]
            
        return lst