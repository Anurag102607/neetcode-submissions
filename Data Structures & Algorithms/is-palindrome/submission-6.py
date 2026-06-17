class Solution:
    def isPalindrome(self, s: str) -> bool:

        # remove spaces and join words
        # reverse str= str then true else false
        # without reverse using two pointer 
        # one from beginning and other from end
        # check one by one if not same return False

        
        if (len(s) == 0):
            return False
        if(len(s)==1):
            return True
        s="".join(ch.lower() for ch in s if ch.isalnum())
        i=0
        j=len(s)-1
        while i<j:
            if s[i] != s[j]:
                return False
            else:
                i=i+1
                j=j-1
        
        return True


        