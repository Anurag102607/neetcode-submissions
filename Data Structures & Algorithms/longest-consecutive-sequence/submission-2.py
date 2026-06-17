class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        count=1
        max_count=1
        # sort the array
        nums.sort()

        # 2,3,4,4,5,10,20  -- 1 
        # i=1 nums=3, count =2...i=2 num=4 and count=3, 
        # i=3 num=4 count=3...i=4 num=5 and count=4
        # i=5 num=10 count=4
        # 0,1,1,2,3,4,5,6
        # i=1 num =1 count=2, i=2 num=1 count=2
        # i=3 num=2 count=3, i=4 num=3 count=4
        #
        if len(nums)==0:
            return 0
        for i in range(1, len(nums)):
            
            if nums[i] == nums[i-1]+1 :
                count += 1
            elif nums[i]==nums[i-1]:
                continue
            else:
                max_count=max(max_count,count)
                count=1
        max_count=max(max_count,count)    
        return max_count




        