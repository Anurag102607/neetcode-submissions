class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen={}
        lst=[]
        for num in nums:

            if num in seen:
                seen[num]=seen[num]+1
            else:
                seen[num]=1

        sorted_items = sorted(seen.items(), key=lambda item: item[1], reverse=True)
        for i in range(0,k):
            lst.append(sorted_items[i][0])
        
        return lst

        