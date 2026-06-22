class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left=0
        right=len(heights)-1
        max_vol=0
        while (left<right):

            vol=(right-left) * min(heights[left] , heights[right])
            
            max_vol= max(max_vol,vol)
            
            if(heights[left] > heights[right]):
                right-=1
            else:
                left+=1
        
        return max_vol


# 1 right 6 vol 5*1 , 5
        
        