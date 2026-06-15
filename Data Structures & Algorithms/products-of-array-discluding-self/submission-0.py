class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod=1
        zero_count=0
        lst=[]
        for num in nums:
            if num ==0:
                zero_count +=1
            else:
                prod =prod*num
        
        for num in nums:
            if zero_count > 1:
                lst.append(0)
            elif zero_count ==1 :
                if num==0:
                    lst.append(prod)
                else:
                    lst.append(0)
            else:
                lst.append(prod//num)
        return lst