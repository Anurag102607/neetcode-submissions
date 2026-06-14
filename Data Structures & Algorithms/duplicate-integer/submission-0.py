class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        set1=set()
        for num in nums:
            set1.add(num)

        if len(nums) != len(set1):
            return True
        else:
            return False
        