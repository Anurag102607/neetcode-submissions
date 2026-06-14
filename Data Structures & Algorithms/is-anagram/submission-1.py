class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count={}

        for c in s:
            if c in count:
                count[c]=count[c]+1
            else:
                count[c]=1
        
        for c in t:

            if c in count:
                count[c]=count[c]-1
            else:
                return False
        
            if count[c] == 0:
                del(count[c])
        
        return (len(count)==0)
        