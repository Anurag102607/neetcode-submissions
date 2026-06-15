class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # using Sorting 
        seen={}
        lst=[]
        for word in strs:

            sorted_lst=sorted(word)
            sorted_word="".join(sorted_lst)

            if sorted_word in seen:
                seen[sorted_word].append(word)
            else:    
                seen[sorted_word]=[word]

        lst = list(seen.values())

        return lst        


